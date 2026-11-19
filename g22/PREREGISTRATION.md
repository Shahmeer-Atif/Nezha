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

## Amendment 1 (2026-11-18 PKT, committed before any round-2 run)

Added after an outside review of the Day-80 draft. No run, definition, hypothesis or analysis in
Sections 1 to 6 is changed, and Component C is unchanged. Every item below is computed from the
same 22 run logs and the alarm lists already produced by `alarm_equivalence.py`; no run is added.

Additional analyses:

- **A1. Service-only accuracy.** Top-k computed from the pod position (Section 2): a fault counts at
  k if the first candidate on the injected pod is at list position k or better, ignoring resource and
  log template. Reported per run for k = 1, 3, 5 next to the original, strict and ordinal values.
  A fault whose injected pod is absent from the candidate list counts as not localized.
- **A2. Per-fault-type table.** For each variant against the baseline of the same system and each
  injected fault type: total cases, baseline matches at rank 1, variant matches at rank 1,
  recoveries (wrong to right) and regressions (right to wrong), using the original rank.
- **A3. Attribution bound.** For each alarm mode (baseline, A, B and AB at k = 3) and each resource
  fault: whether the alarm list of the injected pod in the analysed minute contains the resource
  type named in `construct_data/root_cause_<ns>.json`. The count is an upper bound on the resource
  faults that any rule choosing among the pod's own alarms could match, whatever the ranking.
  Descriptive only; no hypothesis.

Clarifications of wording in Section 4 (fixed here, before data):

- Analysis 4, error split: the error set is every resource fault with no match at list position 1.
  Localization error = pod position > 1; attribution error = pod position 1 and no match at
  position 1. A fault whose injected pod is absent from the list is reported in its own row.
- Analysis 3: top-1 correctness uses the original rank. p-values are reported without a
  multiple-comparison correction, together with the number of tests.
- Q0: the stop condition stays as written (runs 1 and 2 against the round-1 service-level logs).
  Runs 21 and 22 are also compared per case with the round-1 inner-level logs, and runs 18 to 20
  with the round-1 A, B and A+B logs. These comparisons are reported as additional checks.

Checks outside the 22 runs (no effect on any run):

- Unit tests of the released rank rule and of the strict, ordinal and pod-position values on small
  synthetic candidate lists (right pod with wrong resource; non-matching candidate with a resource;
  candidate without a resource; tied scores).
- Recomputation of the shipped `metric_threshold/*.csv` statistics from `construct_data/` with the
  released `generate_threshold` logic, to report whether the shipped means and standard deviations
  can be reproduced from the shipped fault-free data.

A pre-flight run of one baseline configuration (TrainTicket, inner-service level, all switches off)
was made in a scratch directory on 2026-11-18 before this commit, only to confirm that the worker
layout runs and that audit lines are written. It is not one of the 22 runs and is not reported as a result.

## Deviations

1. **Interrupted batch.** The batch was started at 2026-11-17T19:13Z on commit `0175a9d`. After 12 of
   the 22 jobs had finished (01 to 12, all with exit 0) it was stopped by hand at about
   2026-11-18T02:52Z, because the laptop had to be closed. Jobs 13 (OnlineBoutique, B, k = 5) and 14
   (TrainTicket, B, k = 1) were running and were cut off after 43 of 56 and 12 of 45 faults. Their
   two claim folders and their partial output files (two empty stdout files, two time files) were
   deleted, and nothing from them is used. The batch was restarted with the same script and commit at
   2026-11-18T19:50Z. It kept the 12 finished jobs, repeated the setup step (alarm-list equivalence
   for B at k = 1, 2, 4, 5 and the false-alarm probes, with the same outcomes), rebuilt both workers
   from the pristine Drain files and ran jobs 13 to 22 from the start. `round2.log` therefore holds
   two `ROUND2 START` lines, and start lines without exit lines for jobs 13 and 14 from the first
   session. Reason: machine availability. No run configuration, analysis or criterion changed. Every
   job starts from the pristine state and Q0 holds, so no effect on results is expected; wall times
   differ between the sessions and are not compared (Section 6).
2. **Analyses that were not pre-registered.** Three descriptive checks were added after the data were
   seen and are labelled post hoc where they are reported: (a) for B at k = 3 on TrainTicket, the
   alarm lists were inspected by date (alarms of `ts-train-service` in the construction minute and
   in the fault windows, and the first candidate of each lost case); (b) the four round-1
   reproduction logs were compared per case with the authors' shipped reference logs in `log/`;
   (c) the values and thresholds of the alarms were listed for the OnlineBoutique cases that
   Component C changes. They change no pre-registered analysis or criterion.
