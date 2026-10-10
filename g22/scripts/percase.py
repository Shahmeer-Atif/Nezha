"""Per-case rank extraction from a Nezha service-level log.
Returns {inject_time: (service, fault_type, rank or None)}. None = root cause never proposed.
Ranks come from the final rank vector, aligned to the 'score' lines in log order."""
import re, ast, sys
def parse(path):
    L = open(path, errors='ignore').read().split('\n')
    cases = {}
    for l in L:
        m = re.search(r"(\S+ \S+) Inject Ground Truth: (\S+?), (\w+)$", l)
        if m:
            cases.setdefault(m.group(1), (m.group(2).rsplit('-', 2)[0], m.group(3)))
    scored = [re.search(r"(\S+ \S+) Inject Ground Truth: \S+?, \w+ score \d+$", l).group(1)
              for l in L if re.search(r"Inject Ground Truth: \S+?, \w+ score \d+$", l)]
    vec = None
    for l in reversed(L):
        m = re.search(r":\s*(\[\s*\d+(?:\s*,\s*\d+)+\s*\])\s*$", l)
        if m:
            v = ast.literal_eval(m.group(1))
            if len(v) > 5: vec = v; break
    assert vec is not None and len(vec) == len(scored), f"{path}: vec {len(vec) if vec else 0} vs scored {len(scored)}"
    rank = dict(zip(scored, vec))
    return {ts: (svc, ft, rank.get(ts)) for ts, (svc, ft) in cases.items()}
def acc(res, k): return sum(1 for _, _, r in res.values() if r is not None and r <= k)
if __name__ == "__main__":
    a, b = parse(sys.argv[1]), parse(sys.argv[2])
    assert set(a) == set(b), "case sets differ"
    diff = [(ts, a[ts], b[ts]) for ts in sorted(a) if a[ts][2] != b[ts][2]]
    print(f"cases: {len(a)}   differing ranks: {len(diff)}")
    for ts, x, y in diff:
        f = lambda r: 'MISS' if r is None else r
        print(f"   {ts}  {x[0]:24} {x[1]:15} {f(x[2])} -> {f(y[2])}")
    for k in (1, 3, 5): print(f"   @{k}: {acc(a,k)}/{len(a)} -> {acc(b,k)}/{len(b)}")
