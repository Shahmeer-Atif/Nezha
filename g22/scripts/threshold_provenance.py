"""Can the shipped metric_threshold/<service>.csv statistics be reproduced from the shipped data?
Listed in g22/PREREGISTRATION.md, Amendment 1 ("Checks outside the 22 runs"). Reads only.

Usage (from the repository root):  ./.venv/bin/python g22/scripts/threshold_provenance.py

For CPU and memory it applies the released generate_threshold logic (alarm.py): concatenate the
metric files of all pods of a service, then numpy mean and (population) std. It tries each
construction date, each evaluation date and the two dates of a system together, and reports the
candidate source closest to the shipped values. It also reports whether the metric files under
construct_data/ and rca_data/ are the same files, and which time span they cover.
"""
import filecmp, os, sys
import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATES = {"hipster": ("2022-08-22", "2022-08-23"), "ts": ("2023-01-29", "2023-01-30")}
COLS = ["CpuUsageRate(%)", "MemoryUsageRate(%)"]


def svc_of(fname):
    return fname.split("_")[0].rsplit("-", 2)[0]


def frames(base, date):
    d = os.path.join(REPO, base, date, "metric")
    out = {}
    for f in sorted(os.listdir(d)):
        if "metric" in f:
            out.setdefault(svc_of(f), []).append(pd.read_csv(os.path.join(d, f), usecols=["Time"] + COLS))
    return out


def stats(dfs):
    r = pd.concat(dfs)
    return {c: (float(np.mean(r[c])), float(np.std(r[c]))) for c in COLS}


def main():
    print("## Metric files: construction data versus evaluation data\n")
    print("| Date | Files | Byte-identical in construct_data and rca_data | First timestamp | Last timestamp | Rows |")
    print("|---|---|---|---|---|---|")
    data = {}
    for ns, dates in DATES.items():
        for date in dates:
            c = os.path.join(REPO, "construct_data", date, "metric")
            r = os.path.join(REPO, "rca_data", date, "metric")
            names = sorted(f for f in os.listdir(c) if "metric" in f)
            same = sum(1 for f in names if os.path.exists(os.path.join(r, f)) and filecmp.cmp(os.path.join(c, f), os.path.join(r, f), shallow=False))
            data[("construct_data", date)] = frames("construct_data", date)
            data[("rca_data", date)] = frames("rca_data", date)
            allrows = pd.concat([x for v in data[("construct_data", date)].values() for x in v])
            t = allrows["Time"].str.slice(0, 19)
            print(f"| {date} | {len(names)} | {same} of {len(names)} | {t.min()} | {t.max()} | {len(allrows)} |")

    print("\n## Shipped statistics versus recomputation (CPU and memory)\n")
    print("Row 1 of each shipped file is read as the mean and row 2 as the standard deviation, as "
          "written by generate_threshold.\n")
    rows, best_count = [], {}
    for ns, dates in DATES.items():
        cands = {}
        for base in ("construct_data", "rca_data"):
            for date in dates:
                cands[f"{base} {date}"] = data[(base, date)]
            both = {}
            for date in dates:
                for s, v in data[(base, date)].items():
                    both.setdefault(s, []).extend(v)
            cands[f"{base} both dates"] = both
        for s in sorted(set().union(*[set(v) for v in cands.values()])):
            path = os.path.join(REPO, "metric_threshold", s + ".csv")
            if not os.path.exists(path):
                rows.append((ns, s, "no shipped file", "", "", ""))
                continue
            shipped = pd.read_csv(path)
            best = None
            for label, src in cands.items():
                if s not in src:
                    continue
                st = stats(src[s])
                err = max(abs(st[c][i] - float(shipped[c].iloc[i])) for c in COLS for i in (0, 1))
                if best is None or err < best[1]:
                    best = (label, err, st)
            label, err, st = best
            exact = err < 1e-6
            best_count[label if exact else "no exact source"] = best_count.get(label if exact else "no exact source", 0) + 1
            rows.append((ns, s, label, f"{err:.3g}", "yes" if exact else "no",
                         "; ".join(f"{c.split('Usage')[0]} shipped {float(shipped[c].iloc[0]):.2f}/{float(shipped[c].iloc[1]):.2f} "
                                   f"recomputed {st[c][0]:.2f}/{st[c][1]:.2f}" for c in COLS)))
    print("| System | Service | Closest source | Largest absolute difference | Reproduced (< 1e-6) | mean/std |")
    print("|---|---|---|---|---|---|")
    for r in rows:
        print("| " + " | ".join(r) + " |")
    print("\nServices per outcome: " + ", ".join(f"{k}: {v}" for k, v in sorted(best_count.items())))
    shipped_only = sorted(set(f[:-4] for f in os.listdir(os.path.join(REPO, "metric_threshold")) if f.endswith(".csv"))
                          - {r[1] for r in rows})
    print(f"Shipped threshold files with no metric data in either folder: {len(shipped_only)} {shipped_only}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
