"""Unit tests of the released rank rule and of the G22 audit values on small synthetic lists.
Listed in g22/PREREGISTRATION.md, Amendment 1 ("Checks outside the 22 runs").

Run from a COPY of the code directory, because importing the pipeline creates a file in ./log:
    cd <copy of the repository code with log/ and log_template/>
    ./.venv/bin/python <repo>/g22/scripts/evaluator_unit_tests.py

released_rank() is a transcription of the rank loop in pattern_ranker.py (evaluation_pod, the
branches for one-part and two-part root causes). The audit values come from the real
pattern_ranker.g22_audit, called unchanged, with its log call captured.
"""
import os, sys

sys.path.insert(0, os.getcwd())
import pattern_ranker as pr  # noqa: E402

TEMPLATES = {1: "alpha start", 2: "alpha done", 3: "Start charge card", 4: "Charge successfully"}
pr.from_id_to_template = lambda i, miner: TEMPLATES[i]


class Capture:
    def info(self, fmt, *args):
        self.args = args


def released_rank(result_list, inject_pod, root_cause):
    """Rank as computed by the released evaluator; None when no candidate matches."""
    topk = 1
    if len(root_cause) == 1:
        for i in range(len(result_list)):
            if "resource" in result_list[i].keys():
                if str(root_cause[0]) in str(result_list[i]["resource"]) and str(inject_pod) in str(result_list[i]["pod"]):
                    return topk
            else:
                if i > 0:
                    if result_list[i-1]["score"] == result_list[i]["score"] and result_list[i-1]["deepth"] == result_list[i]["deepth"]:
                        continue
                    else:
                        topk = topk + 1
                elif i == 0:
                    topk = topk + 1
    elif len(root_cause) == 2:
        for i in range(len(result_list)):
            ev = result_list[i]["events"].split("_")
            if root_cause[0] in TEMPLATES[int(ev[0])] and root_cause[1] in TEMPLATES[int(ev[1])] and str(inject_pod) in str(result_list[i]["pod"]):
                return topk
            else:
                if i > 0:
                    if result_list[i-1]["score"] == result_list[i]["score"] and result_list[i-1]["deepth"] == result_list[i]["deepth"]:
                        continue
                    else:
                        topk = topk + 1
                elif i == 0:
                    topk = topk + 1
    return None


def cand(pod, score, resource=None, deepth=1, events="1_2"):
    c = {"events": events, "score": score, "deepth": deepth, "pod": pod}
    if resource:
        c["resource"] = resource
    return c


A, B, C, D = "svc-a-1111-aaaa", "svc-b-2222-bbbb", "svc-c-3333-cccc", "svc-d-4444-dddd"
CPU, MEM, NET = "CpuUsageRate(%)", "MemoryUsageRate(%)", "NetworkP90(ms)"
RES, CODE = [CPU], ["Start charge card", "Charge successfully"]

# name, candidate list (already sorted), root cause, expected (released, strict, ordinal, pod position)
TESTS = [
    ("match at position 1", [cand(A, 9, CPU)], RES, (1, 1, 1, 1)),
    ("right pod, wrong resource", [cand(A, 9, NET), cand(B, 5, CPU)], RES, (None, None, None, 1)),
    ("one non-matching candidate with a resource ahead", [cand(B, 9, MEM), cand(A, 5, CPU)], RES, (1, 2, 2, 2)),
    ("three non-matching candidates with a resource ahead",
     [cand(B, 9, MEM), cand(C, 8, NET), cand(D, 7, CPU), cand(A, 5, CPU)], RES, (1, 4, 4, 4)),
    ("one candidate without a resource ahead", [cand(B, 9), cand(A, 5, CPU)], RES, (2, 2, 2, 2)),
    ("two tied candidates without a resource ahead", [cand(B, 9), cand(C, 9), cand(A, 5, CPU)], RES, (2, 2, 3, 3)),
    ("one without and one with a resource ahead", [cand(B, 9), cand(C, 8, MEM), cand(A, 5, CPU)], RES, (2, 3, 3, 3)),
    ("code fault, candidate with a resource ahead",
     [cand(B, 9, MEM), cand(A, 5, events="3_4")], CODE, (2, 2, 2, 2)),
    ("code fault, right pod but wrong log pattern", [cand(A, 9, events="1_2")], CODE, (None, None, None, 1)),
]


def main():
    cap = Capture()
    pr.logger = cap
    failed = 0
    print("| Case | Released rank | Strict rank | Ordinal position | Pod position | As expected |")
    print("|---|---|---|---|---|---|")
    for name, lst, root, expected in TESTS:
        fault = {"inject_time": "t", "inject_pod": A, "inject_type": "x"}
        pr.g22_audit(lst, fault, root, None)
        got = (released_rank(lst, A, root), cap.args[3], cap.args[4], cap.args[5])
        ok = got == expected
        failed += not ok
        show = lambda v: "none" if v is None else v
        print(f"| {name} | {show(got[0])} | {show(got[1])} | {show(got[2])} | {show(got[3])} | {'yes' if ok else 'NO, expected ' + str(expected)} |")
    print(f"\n{len(TESTS) - failed} of {len(TESTS)} cases as expected")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
