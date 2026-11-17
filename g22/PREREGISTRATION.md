# G22 pre-registration: second experiment round (November 2026)

Written and committed **before** any run of this round. Every analysis below is fixed in advance.
Any deviation will be listed under "Deviations" at the end of this file, with its reason, in a later commit.

Base: branch `g22-alarm-study` at commit `f75c45f` (results of round 1: reproduction, failure analysis,
A/B/A+B ablation on OnlineBoutique at service level, k = 3).

## 1. Questions and hypotheses

| ID | Question | Hypothesis |
|---|---|---|
| Q0 | Does the modified code reproduce the released behaviour exactly when every G22 switch is off? | Per-case ranks equal the round-1 reproduction logs for both systems at service level. |
| Q1 | Does the round-1 alarm-stage result hold on TrainTicket? | A, B and A+B at k = 3 on TrainTicket, service level. No directional hypothesis. |
| Q2 | Does B's outcome depend on the threshold multiplier k? | B at k in {1, 2, 4, 5} on both systems, service level. No directional hypothesis. |
| Q3 | Does attributing the resource by relative exceedance (Component C) recover diagnoses without regressions? | A+C recovers the OnlineBoutique adservice network-delay fault and loses no diagnosis that the baseline gets right at rank 1. |
| Q4 | How much do the released evaluator's rank rules affect reported accuracy? | Logging-only audit; no directional hypothesis. |
| Q5 | Do the variants raise alarms in fault-free windows? | Count only; no hypothesis. |

C was designed after inspecting OnlineBoutique cases only. TrainTicket results for C are therefore
treated as the held-out evaluation; OnlineBoutique results for C are reported as in-sample.

## 2. Definitions

- **Component C** (`NEZHA_ATTRIBUTION=ratio`, `alarm.py: attributed_resource`): when a pod carries more
  than one alarm, the resource attached to its ranked candidates is the alarm with the largest
  `value / threshold`, where `threshold` is the threshold that raised the alarm (80 % CPU/memory,
  200 ms / 300 ms network, or mean + k·std under B). Ties keep the original order (CPU, memory,
  network). C does not change alarm events, event graphs or pattern scores. With one alarm per pod
  (baseline or B without A) C has no effect, so C is evaluated only as A+C and A+B+C.
- **Original rank**: the rank produced by the released evaluator (unchanged).
- **Strict rank** (audit): the released rule with one change: a non-matching candidate that carries a
  resource advances the rank counter like any other non-matching candidate. Score/depth tie handling
  is unchanged.
- **Ordinal position** (audit): 1-based position of the first matching candidate in the sorted list.
- **Pod position** (audit): 1-based position of the first candidate on the injected pod, ignoring
  resource and log template. Used to split errors into localization (wrong pod first) and
  attribution (right pod first, wrong resource or template).
- All three audit values are written as `G22-AUDIT` log lines; the original rank and the reported
  AS@k/AIS@k are computed exactly as before.

## 3. Runs (service level unless stated; one run per configuration)

The pipeline contains no random-number generation and round 1 reproduced the authors' per-case
ranks, so configurations are run once. Q0 re-checks determinism. Drain state is restored from the
pristine files (hashes in `provenance/drain3-pristine-sha256.txt`) before every run.

| # | System | Mode | k | Attribution | Purpose |
|---|---|---|---|---|---|
| 1 | OnlineBoutique | baseline | n/a | first | Q0, Q4 |
| 2 | TrainTicket | baseline | n/a | first | Q0, Q4 |
| 3 | OnlineBoutique | A | n/a | ratio | Q3 (in-sample) |
| 4 | TrainTicket | A | n/a | ratio | Q3 (held-out) |
| 5 | OnlineBoutique | AB | 3 | ratio | Q3 (in-sample) |
| 6 | TrainTicket | AB | 3 | ratio | Q3 (held-out) |
| 7-9 | TrainTicket | A, B, AB | 3 | first | Q1 |
| 10-13 | OnlineBoutique | B | 1, 2, 4, 5 | first | Q2 |
| 14-17 | TrainTicket | B | 1, 2, 4, 5 | first | Q2 |
| 18-20 | OnlineBoutique | A, B, AB | 3 | first | rerun of round 1 with audit logging |
| 21-22 | TrainTicket, OnlineBoutique | baseline, inner-service level | n/a | first | Q4 at inner level |

Q5: `g22/scripts/fa_probe.py` for baseline, A, B (k = 1..5) and AB (k = 3).
Alarm-list equivalence (`g22/scripts/alarm_equivalence.py`): the current `alarm.py` is compared with
`provenance/alarm_as_tested_for_AB_runs.py` on all 105 analysed minutes for every mode and k used.

## 4. Analyses

1. AS@1/3/5 (AIS@1/3/5 for runs 21-22) as counts and percentages, per run.
2. Per-case rank changes against the baseline of the same system (`g22/scripts/percase.py`).
3. McNemar exact test (two-sided, binomial on discordant pairs) on top-1 correctness, each variant
   versus the baseline of the same system. With 56 and 45 faults the test has low power; non-significant
   results will be reported as such, not as evidence of no effect.
4. Audit (Q4): AS@k recomputed from strict ranks and from ordinal positions, next to the original
   AS@k, for every run. Error split at k = 1 for resource faults: localization error (pod position > 1)
   versus attribution error (pod position = 1, no match at position 1).
5. Q3 success criteria for C, fixed here: (a) the adservice network-delay fault of 2022-08-23 16:05:02
   is diagnosed at rank 1 under A+C; (b) no fault correct at rank 1 under the baseline is lost under
   A+C, on either system; (c) AS@1 under A+C is not lower than the baseline on either system.
   C is reported as successful only if all three hold; partial outcomes are reported per criterion.

## 5. Pre-run observations (made before this commit, on OnlineBoutique only)

A unit check of `attributed_resource` under mode A on the three OnlineBoutique diagnostic windows
(analysis minutes 2022-08-23 16:07, 12:55 and 13:29) gave, as (value, threshold):

| Service (fault) | Alarms under A | First (original) | Ratio (C) | Required |
|---|---|---|---|---|
| adservice (network_delay) | memory (87.1, 80), network (512.0, 200) | memory | network | network |
| checkoutservice (network_delay) | network (235.7, 200) | network | network | network |
| currencyservice (cpu_contention) | CPU (85.0, 80), network (1403.2, 200) | CPU | network | CPU |

Prediction recorded before the runs: A+C is expected to recover adservice and to **lose** the
currencyservice cpu_contention diagnosis, so criterion 4.5(b) is expected to fail on OnlineBoutique.
CPU contention on currencyservice also raises its network latency far above the network threshold,
so relative exceedance does not separate the cause from a propagated symptom in this case.

C is not modified in response. A z-score variant ((x - mean) / std) was considered and rejected
before any run: the shipped baseline statistics give network a standard deviation of 0 for these
services, so a network z-score is undefined without an arbitrary floor, and choosing that floor
after this observation would fit the method to the evaluation data. TrainTicket remains the
held-out evaluation for C.

## 6. Reporting commitments

- Every run in Section 3 is reported, including failed or unfavourable outcomes.
- Runtime is not compared: two runs execute in parallel, so wall times are not controlled.
- Logs, per-case tables and analysis scripts are committed to `g22/logs/` and `g22/scripts/`.

## Deviations

None yet.
