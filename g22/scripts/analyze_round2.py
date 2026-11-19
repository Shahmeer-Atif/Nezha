"""Round-2 analysis, exactly as fixed in g22/PREREGISTRATION.md (Section 4 and Amendment 1).

Usage (from the repository root):
    ./.venv/bin/python g22/scripts/analyze_round2.py [--res g22/logs/round2] [--out DIR]

Reads the run logs only. Writes report.md and percase.csv to --out (default: <res>/analysis).
Written before any round-2 run existed; tested on round-1 logs and one pre-flight log.
"""
import argparse, csv, datetime, json, os, re, sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import percase  # noqa: E402  (per-case rank extraction used in round 1)

# tag, system, level, mode, k, attribution  (same list as run_round2.sh)
JOBS = [l.split() for l in """
01_hipster_service_baseline hipster service baseline 3 first
02_ts_service_baseline ts service baseline 3 first
03_hipster_service_A_ratio hipster service A 3 ratio
04_ts_service_A_ratio ts service A 3 ratio
05_hipster_service_AB_k3_ratio hipster service AB 3 ratio
06_ts_service_AB_k3_ratio ts service AB 3 ratio
07_ts_service_A ts service A 3 first
08_ts_service_B_k3 ts service B 3 first
09_ts_service_AB_k3 ts service AB 3 first
10_hipster_service_B_k1 hipster service B 1 first
11_hipster_service_B_k2 hipster service B 2 first
12_hipster_service_B_k4 hipster service B 4 first
13_hipster_service_B_k5 hipster service B 5 first
14_ts_service_B_k1 ts service B 1 first
15_ts_service_B_k2 ts service B 2 first
16_ts_service_B_k4 ts service B 4 first
17_ts_service_B_k5 ts service B 5 first
18_hipster_service_A hipster service A 3 first
19_hipster_service_B_k3 hipster service B 3 first
20_hipster_service_AB_k3 hipster service AB 3 first
21_ts_inner_baseline ts inner baseline 3 first
22_hipster_inner_baseline hipster inner baseline 3 first
""".strip().split("\n")]
BASE = {"hipster": "01_hipster_service_baseline", "ts": "02_ts_service_baseline"}
NFAULT = {"hipster": 56, "ts": 45}
NAME = {"hipster": "OnlineBoutique", "ts": "TrainTicket"}
R1 = os.path.join(REPO, "g22", "logs")
ROUND1 = {  # round-2 tag -> round-1 log it must equal per case
    "01_hipster_service_baseline": "reproduction/OnlineBoutique_service_nezha.log",
    "02_ts_service_baseline": "reproduction/TrainTicket_service_nezha.log",
    "21_ts_inner_baseline": "reproduction/TrainTicket_inner_nezha.log",
    "22_hipster_inner_baseline": "reproduction/OnlineBoutique_inner_nezha.log",
    "18_hipster_service_A": "ablation/A_k3_hipster_service_nezha.log",
    "19_hipster_service_B_k3": "ablation/B_k3_hipster_service_nezha.log",
    "20_hipster_service_AB_k3": "ablation/AB_k3_hipster_service_nezha.log",
}
Q0_GATE = ("01_hipster_service_baseline", "02_ts_service_baseline")
ADSERVICE_CASE = "2022-08-23 16:05:02"
AUDIT_RE = re.compile(r"G22-AUDIT (\S+ \S+) \| (\S+) \| (\w+) \| strict=(\S+) ordinal=(\S+) "
                      r"podpos=(\S+) n=(\d+) top_pod=(\S+) top_resource=(.*)$")


def _int(s):
    return None if s == "None" else int(s)


def load_run(path):
    """{inject_time: dict(svc, type, rank, strict, ordinal, podpos, pod)}, reported %, has_audit."""
    cases = {ts: {"svc": svc, "type": ft, "rank": r, "strict": None, "ordinal": None,
                  "podpos": None, "pod": None, "audit": False}
             for ts, (svc, ft, r) in percase.parse(path).items()}
    lines = open(path, errors="ignore").read().split("\n")
    n_audit = 0
    for l in lines:
        m = AUDIT_RE.search(l)
        if m and m.group(1) in cases and not cases[m.group(1)]["audit"]:
            cases[m.group(1)].update(pod=m.group(2), strict=_int(m.group(4)), ordinal=_int(m.group(5)),
                                     podpos=_int(m.group(6)), audit=True)
            n_audit += 1
    reported = []
    for i, l in enumerate(lines):
        if re.search(r"S@[135] Result", l) and i + 1 < len(lines):
            m = re.search(r"([0-9.]+) %", lines[i + 1])
            reported.append(float(m.group(1)) if m else None)
    return cases, reported, n_audit


def at_k(cases, field, k):
    return sum(1 for c in cases.values() if c[field] is not None and c[field] <= k)


def fmt(n, total):
    return f"{n}/{total} ({100 * n / total:.2f}%)"


def mcnemar_exact(b, c):
    """Two-sided exact binomial test on the discordant pairs (b, c)."""
    n = b + c
    if n == 0:
        return 1.0
    return min(1.0, 2 * sum(comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)


def root_causes():
    return {ns: json.load(open(os.path.join(REPO, "construct_data", f"root_cause_{ns}.json")))
            for ns in ("hipster", "ts")}


def is_resource_fault(rc, ns, svc, ftype):
    return len(rc[ns][svc][ftype].split("_")) == 1


def show(r):
    return "MISS" if r is None else str(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--res", default=os.path.join(REPO, "g22", "logs", "round2"))
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    res, out = a.res, a.out or os.path.join(a.res, "analysis")
    os.makedirs(out, exist_ok=True)
    rc = root_causes()
    W = []  # report lines
    P = W.append

    # ---------- 0. completion ----------
    P("# Round 2 analysis\n")
    P(f"Generated {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} by `g22/scripts/analyze_round2.py` "
      f"from `{os.path.relpath(res, REPO)}`.\n")
    P("## 0. Completion\n")
    rlog = os.path.join(res, "round2.log")
    logtxt = open(rlog).read() if os.path.exists(rlog) else ""
    exits = dict(re.findall(r"^\s+(\S+) exit=(-?\d+)", logtxt, flags=re.M))
    runs, problems = {}, []
    for tag, ns, level, mode, k, attr in JOBS:
        path = os.path.join(res, f"{tag}_nezha.log")
        if exits.get(tag) != "0":
            problems.append(f"{tag}: exit={exits.get(tag, 'no exit line')}")
        if not os.path.exists(path):
            problems.append(f"{tag}: log file missing")
            continue
        try:
            cases, reported, n_audit = load_run(path)
        except Exception as e:  # report, do not hide
            problems.append(f"{tag}: log not parseable ({e})")
            continue
        if len(cases) != NFAULT[ns]:
            problems.append(f"{tag}: {len(cases)} cases, expected {NFAULT[ns]}")
        if n_audit != len(cases):
            problems.append(f"{tag}: {n_audit} audit lines for {len(cases)} cases")
        runs[tag] = dict(ns=ns, level=level, mode=mode, k=k, attr=attr, cases=cases, reported=reported)
    done = "ROUND2 DONE" in logtxt
    P(f"- `ROUND2 DONE` present: **{done}**; start lines: {len(re.findall('ROUND2 START', logtxt))}")
    P(f"- jobs with exit=0: **{sum(1 for t in exits.values() if t == '0')} of {len(JOBS)}**; "
      f"logs parsed: {len(runs)} of {len(JOBS)}")
    P("- problems: " + ("**none**" if not problems else ""))
    for p in problems:
        P(f"  - {p}")
    P("")

    # ---------- 1. Q0 ----------
    P("## 1. Q0: switches off and reruns against round 1 (per case)\n")
    P("| Round-2 run | Round-1 log | Cases | Differing ranks | Role |")
    P("|---|---|---|---|---|")
    q0_ok = True
    for tag, rel in ROUND1.items():
        role = "Q0 stop condition" if tag in Q0_GATE else "additional check (Amendment 1)"
        if tag not in runs:
            P(f"| {tag} | {rel} | n/a | RUN MISSING | {role} |")
            q0_ok = q0_ok and tag not in Q0_GATE
            continue
        old = percase.parse(os.path.join(R1, rel))
        new = runs[tag]["cases"]
        same_set = set(old) == set(new)
        diff = [ts for ts in sorted(set(old) & set(new)) if old[ts][2] != new[ts]["rank"]]
        P(f"| {tag} | {rel} | {len(new)}{'' if same_set else ' (case sets differ)'} | {len(diff)} | {role} |")
        for ts in diff:
            P(f"|  | {ts} {new[ts]['svc']} {new[ts]['type']} | | {show(old[ts][2])} -> {show(new[ts]['rank'])} | |")
        if tag in Q0_GATE and (diff or not same_set):
            q0_ok = False
    P(f"\n**Q0 stop condition (runs 1 and 2 equal round 1 per case): {'PASS' if q0_ok else 'FAIL - stop and report'}**\n")

    # ---------- 2. accuracy, audit, service-only ----------
    P("## 2. Accuracy per run (analysis 1, analysis 4, Amendment A1)\n")
    P("Original = released evaluator. Strict, ordinal and pod-only come from the `G22-AUDIT` lines. "
      "AIS for the inner-level runs 21 and 22.\n")
    P("| Run | System | Level | Mode | k | Attr | Original @1 | @3 | @5 | Log says @1/@3/@5 | Strict @1 | @3 | @5 "
      "| Ordinal @1 | @3 | @5 | Pod-only @1 | @3 | @5 |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for tag, ns, level, mode, k, attr in JOBS:
        if tag not in runs:
            P(f"| {tag} | {NAME[ns]} | {level} | {mode} | {k} | {attr} | MISSING |||||||||||||")
            continue
        c, n = runs[tag]["cases"], len(runs[tag]["cases"])
        rep = " / ".join(f"{x:.2f}" if x is not None else "?" for x in runs[tag]["reported"])
        cells = [fmt(at_k(c, f, kk), n) for f in ("rank",) for kk in (1, 3, 5)]
        cells.append(rep)
        cells += [fmt(at_k(c, f, kk), n) for f in ("strict", "ordinal", "podpos") for kk in (1, 3, 5)]
        kshow = k if "B" in mode else "n/a"
        P(f"| {tag[:2]} | {NAME[ns]} | {level} | {mode} | {kshow} | {attr} | " + " | ".join(cells) + " |")
    P("")
    P("Cases where the original rank and the strict rank or ordinal position disagree:\n")
    P("| Run | Case | Service | Fault | Original | Strict | Ordinal | Pod position |")
    P("|---|---|---|---|---|---|---|---|")
    nd = 0
    for tag, *_ in JOBS:
        for ts, c in sorted(runs.get(tag, {}).get("cases", {}).items()):
            if c["audit"] and not (c["rank"] == c["strict"] == c["ordinal"]):
                nd += 1
                P(f"| {tag[:2]} | {ts} | {c['svc']} | {c['type']} | {show(c['rank'])} | {show(c['strict'])} "
                  f"| {show(c['ordinal'])} | {show(c['podpos'])} |")
    P(f"\nTotal disagreeing case-runs: {nd}\n")

    # ---------- 3. per-case changes, 4. McNemar ----------
    P("## 3. Per-case rank changes against the baseline of the same system (analysis 2)\n")
    mc = []
    for tag, ns, level, mode, k, attr in JOBS:
        if level != "service" or tag == BASE[ns] or tag not in runs or BASE[ns] not in runs:
            continue
        b, v = runs[BASE[ns]]["cases"], runs[tag]["cases"]
        common = sorted(set(b) & set(v))
        diff = [ts for ts in common if b[ts]["rank"] != v[ts]["rank"]]
        P(f"**{tag}**: {len(diff)} of {len(common)} cases changed")
        for ts in diff:
            P(f"- {ts} {v[ts]['svc']} {v[ts]['type']}: {show(b[ts]['rank'])} -> {show(v[ts]['rank'])}")
        P("")
        lost = sum(1 for ts in common if b[ts]["rank"] == 1 and v[ts]["rank"] != 1)
        gained = sum(1 for ts in common if b[ts]["rank"] != 1 and v[ts]["rank"] == 1)
        mc.append((tag, lost, gained, mcnemar_exact(lost, gained)))
    P("## 4. McNemar exact test on top-1 correctness, variant against baseline (analysis 3)\n")
    P(f"Two-sided exact binomial on discordant pairs, original rank. {len(mc)} tests, no multiple-comparison "
      "correction. With 56 and 45 faults the test has low power: a non-significant result is not evidence "
      "of no effect.\n")
    P("| Variant run | Baseline right, variant wrong | Baseline wrong, variant right | p |")
    P("|---|---|---|---|")
    for tag, lost, gained, p in mc:
        P(f"| {tag} | {lost} | {gained} | {p:.4f}{' (no discordant pairs)' if lost + gained == 0 else ''} |")
    P("")

    # ---------- 5. error split ----------
    P("## 5. Error split at position 1 for resource faults (analysis 4)\n")
    P("Error set: resource faults with no match at list position 1. Localization = pod position > 1; "
      "attribution = pod position 1; pod absent = injected pod not in the candidate list.\n")
    P("| Run | Resource faults | Errors | Localization | Attribution | Pod absent |")
    P("|---|---|---|---|---|---|")
    for tag, ns, *_ in JOBS:
        if tag not in runs:
            continue
        rf = [c for c in runs[tag]["cases"].values() if c["audit"] and is_resource_fault(rc, ns, c["svc"], c["type"])]
        err = [c for c in rf if c["ordinal"] != 1]
        P(f"| {tag} | {len(rf)} | {len(err)} | {sum(1 for c in err if c['podpos'] and c['podpos'] > 1)} "
          f"| {sum(1 for c in err if c['podpos'] == 1)} | {sum(1 for c in err if c['podpos'] is None)} |")
    P("")

    # ---------- 6. Component C ----------
    P("## 6. Component C success criteria (analysis 5)\n")
    P("Recorded prediction: A+C recovers adservice and loses currencyservice cpu_contention, so (b) fails on "
      "OnlineBoutique. OnlineBoutique is in-sample, TrainTicket is held-out.\n")
    for label, pair in (("A+C", {"hipster": "03_hipster_service_A_ratio", "ts": "04_ts_service_A_ratio"}),
                        ("A+B+C at k=3 (descriptive; the criteria are defined for A+C)",
                         {"hipster": "05_hipster_service_AB_k3_ratio", "ts": "06_ts_service_AB_k3_ratio"})):
        P(f"**{label}**\n")
        verdicts = []
        if pair["hipster"] in runs:
            r = runs[pair["hipster"]]["cases"].get(ADSERVICE_CASE, {}).get("rank")
            verdicts.append(r == 1)
            P(f"- (a) adservice {ADSERVICE_CASE} at rank 1: **{'HOLDS' if r == 1 else 'FAILS'}** (rank {show(r)})")
        for crit in ("b", "c"):
            for ns in ("hipster", "ts"):
                if pair[ns] not in runs or BASE[ns] not in runs:
                    P(f"- ({crit}) {NAME[ns]}: run missing")
                    verdicts.append(False)
                    continue
                b, v = runs[BASE[ns]]["cases"], runs[pair[ns]]["cases"]
                if crit == "b":
                    lost = [ts for ts in sorted(b) if b[ts]["rank"] == 1 and v.get(ts, {}).get("rank") != 1]
                    verdicts.append(not lost)
                    P(f"- (b) no baseline rank-1 fault lost, {NAME[ns]}: **{'HOLDS' if not lost else 'FAILS'}**"
                      + "".join(f"\n  - lost: {ts} {b[ts]['svc']} {b[ts]['type']} -> {show(v[ts]['rank'])}" for ts in lost))
                else:
                    ok = at_k(v, "rank", 1) >= at_k(b, "rank", 1)
                    verdicts.append(ok)
                    P(f"- (c) AS@1 not below baseline, {NAME[ns]}: **{'HOLDS' if ok else 'FAILS'}** "
                      f"({at_k(b, 'rank', 1)} -> {at_k(v, 'rank', 1)})")
        if label == "A+C":
            P(f"\n**C successful (all three criteria hold): {'YES' if verdicts and all(verdicts) else 'NO'}**")
        P("")

    # ---------- 7. k sweep, alarm counts, false alarms, equivalence ----------
    P("## 7. Threshold multiplier k, alarm counts and fault-free windows (Q2, Q5)\n")
    ktag = {("hipster", "1"): "10", ("hipster", "2"): "11", ("hipster", "3"): "19", ("hipster", "4"): "12",
            ("hipster", "5"): "13", ("ts", "1"): "14", ("ts", "2"): "15", ("ts", "3"): "08", ("ts", "4"): "16",
            ("ts", "5"): "17"}
    bytag = {t[:2]: t for t, *_ in JOBS}

    def alarm_counts(path):
        """alarms per system over fault windows, and in fault-free construction windows."""
        d = json.load(open(path))
        cnt = {ns: [0, 0] for ns in ("hipster", "ts")}
        for key, pods in d["alarms"].items():
            ns, base = key.split(" ")[0], key.split(" ")[-1]
            cnt[ns][0 if base == "rca_data" else 1] += sum(len(x[1]) for x in pods)
        return d["windows"], cnt

    P("| System | Variant | Original @1 | @3 | @5 | Alarms in fault windows | Alarms in the 2 fault-free windows |")
    P("|---|---|---|---|---|---|---|")
    eq_notes = []
    for ns in ("hipster", "ts"):
        rows = [("baseline", BASE[ns], os.path.join(R1, "equivalence", "baseline_k3_alarm.json"))]
        for k in "12345":
            src = os.path.join(R1, "equivalence", "B_k3_alarm.json") if k == "3" else \
                os.path.join(res, "equivalence", f"B_k{k}_alarm.json")
            rows.append((f"B, k={k}", bytag[ktag[(ns, k)]], src))
        for label, tag, src in rows:
            acc = [fmt(at_k(runs[tag]["cases"], "rank", kk), len(runs[tag]["cases"])) for kk in (1, 3, 5)] \
                if tag in runs else ["MISSING"] * 3
            try:
                _, cnt = alarm_counts(src)
                al = [str(cnt[ns][0]), str(cnt[ns][1])]
            except Exception as e:
                al = [f"unreadable ({type(e).__name__})", ""]
            P(f"| {NAME[ns]} | {label} | " + " | ".join(acc + al) + " |")
    P("")
    P("Alarm-list equivalence of the current `alarm.py` with the round-1 implementation (B at k = 1, 2, 4, 5):\n")
    for k in "1245":
        f1 = os.path.join(res, "equivalence", f"B_k{k}_alarm.json")
        f2 = os.path.join(res, "equivalence", f"B_k{k}_alarm_as_tested.json")
        try:
            w1, _ = alarm_counts(f1)
            w2, _ = alarm_counts(f2)
            same = open(f1).read() == open(f2).read()
            P(f"- k={k}: {'IDENTICAL' if same else 'DIFFERENT'}; windows {w1} and {w2} (expected 105)"
              + ("" if w1 == w2 == 105 else " **CHECK**"))
        except Exception as e:
            P(f"- k={k}: **NOT VALID** ({type(e).__name__}: {e})")
    P("\nFalse-alarm probes (alarms in each fault-free construction minute):\n")
    P("| Probe file | Mode | " + "Minute: pods / alarms |")
    P("|---|---|---|")
    for spec in ("baseline_k3", "A_k3", "B_k1", "B_k2", "B_k3", "B_k4", "B_k5", "AB_k3"):
        f = os.path.join(res, f"fa_{spec}.json")
        try:
            d = json.load(open(f))
            P(f"| fa_{spec}.json | {d['mode']} | " + "; ".join(
                f"{t} ({v['ns']}): {v['pods']} / {v['alarms']}" for t, v in sorted(d["result"].items())) + " |")
        except Exception as e:
            P(f"| fa_{spec}.json | | **NOT VALID** ({type(e).__name__}) |")
    P("")

    # ---------- 8. per fault type (Amendment A2) ----------
    P("## 8. Per-fault-type recoveries and regressions at rank 1 (Amendment A2)\n")
    P("| Variant run | Fault type | Cases | Baseline right | Variant right | Recoveries | Regressions |")
    P("|---|---|---|---|---|---|---|")
    for tag, ns, level, *_ in JOBS:
        if level != "service" or tag == BASE[ns] or tag not in runs or BASE[ns] not in runs:
            continue
        b, v = runs[BASE[ns]]["cases"], runs[tag]["cases"]
        for ft in sorted({c["type"] for c in b.values()}):
            ts_ = [ts for ts in b if b[ts]["type"] == ft and ts in v]
            P(f"| {tag} | {ft} | {len(ts_)} | {sum(1 for t in ts_ if b[t]['rank'] == 1)} "
              f"| {sum(1 for t in ts_ if v[t]['rank'] == 1)} "
              f"| {sum(1 for t in ts_ if b[t]['rank'] != 1 and v[t]['rank'] == 1)} "
              f"| {sum(1 for t in ts_ if b[t]['rank'] == 1 and v[t]['rank'] != 1)} |")
    P("")

    # ---------- 9. attribution bound (Amendment A3) ----------
    P("## 9. Attribution bound from the alarm lists (Amendment A3)\n")
    P("For each resource fault: does the injected pod's alarm list in the analysed minute contain the true "
      "resource type? No rule that picks among the pod's own alarms can match more faults than this.\n")
    P("| System | Alarm mode (k=3) | Resource faults | Pod has any alarm | True resource among its alarms (bound) "
      "| True resource is the first alarm |")
    P("|---|---|---|---|---|---|")
    faults = []
    for ns, days in (("hipster", ("2022-08-22", "2022-08-23")), ("ts", ("2023-01-29", "2023-01-30"))):
        for day in days:
            d = json.load(open(os.path.join(REPO, "rca_data", day, day + "-fault_list.json")))
            for group in d.values():
                for f in group:
                    svc = f["inject_pod"].rsplit("-", 2)[0]
                    if is_resource_fault(rc, ns, svc, f["inject_type"]):
                        t = datetime.datetime.strptime(f["inject_time"], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=2)
                        faults.append((ns, f"{ns} {t.strftime('%Y-%m-%d %H:%M')} rca_data", f["inject_pod"],
                                       rc[ns][svc][f["inject_type"]]))
    for ns in ("hipster", "ts"):
        for mode in ("baseline", "A", "B", "AB"):
            try:
                al = json.load(open(os.path.join(R1, "equivalence", f"{mode}_k3_alarm.json")))["alarms"]
            except Exception as e:
                P(f"| {NAME[ns]} | {mode} | unreadable ({type(e).__name__}) ||||")
                continue
            mine = [f for f in faults if f[0] == ns]
            anyal = bound = first = 0
            for _, key, pod, true in mine:
                types = next((x[1] for x in al.get(key, []) if x[0] == pod), [])
                anyal += bool(types)
                bound += any(true in t for t in types)
                first += bool(types) and true in types[0]
            P(f"| {NAME[ns]} | {mode} | {len(mine)} | {anyal} | {bound} | {first} |")
    P("")

    with open(os.path.join(out, "report.md"), "w") as f:
        f.write("\n".join(W) + "\n")
    with open(os.path.join(out, "percase.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["run", "system", "level", "mode", "k", "attribution", "inject_time", "service", "fault_type",
                    "original_rank", "strict_rank", "ordinal_position", "pod_position"])
        for tag, ns, level, mode, k, attr in JOBS:
            for ts, c in sorted(runs.get(tag, {}).get("cases", {}).items()):
                w.writerow([tag, ns, level, mode, k, attr, ts, c["svc"], c["type"], c["rank"], c["strict"],
                            c["ordinal"], c["podpos"]])
    print(f"wrote {out}/report.md and percase.csv; problems: {len(problems)}; Q0 {'PASS' if q0_ok else 'FAIL'}")
    return 0 if (not problems and q0_ok and done) else 1


if __name__ == "__main__":
    sys.exit(main())
