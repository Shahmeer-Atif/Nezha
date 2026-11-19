# G22: Reproduction and Alarm-Stage Study of Nezha

This branch extends [Nezha](https://github.com/IntelligentDDS/Nezha) (Yu et al., ESEC/FSE 2023) for a
research assignment in Cloud Computing at FAST NUCES Islamabad.

**Authors:** Shahmeer Atif (23i-0711) and Taaha Zaman Khan (22i-1377), Group G22.
**Licence:** the original MIT licence and copyright notice are retained. All credit for Nezha belongs to its authors.

The study has two rounds. Round 1 reproduced the paper and tested two alarm-stage changes on one
system. Round 2 (November 2026) was pre-registered in [`PREREGISTRATION.md`](PREREGISTRATION.md)
before any run and covers 22 runs on both systems. **All three tested changes give negative results.**

## What changed

Three files are modified. With no environment variables set, every per-case rank and every reported
accuracy value is identical to the original; the only addition is one `G22-AUDIT` log line per fault.

| File | Change |
|---|---|
| `alarm.py` | `NEZHA_ALARM_MODE` = `baseline` (default), `A`, `B` or `AB`; `NEZHA_K` (default 3); `NEZHA_ATTRIBUTION` = `first` (default) or `ratio`; `NEZHA_MODALITY` metric switch |
| `pattern_ranker.py` | Uses the attribution rule for the resource of a candidate; writes the audit line. The released rank and accuracy code is untouched. |
| `data_integrate.py` | `NEZHA_MODALITY` log switch |

- **A**: `generate_alarm` keeps every alarming metric per pod. The original keeps only the first.
- **B**: CPU and memory alarms use per-service `mean + k * std` from `metric_threshold/<service>.csv`,
  instead of a fixed 80 %. Falls back to 80 % where no usable baseline exists.
- **C** (`NEZHA_ATTRIBUTION=ratio`): when a pod carries more than one alarm, a candidate is labelled
  with the alarm that has the largest `value / threshold`. The original uses the first alarm in the
  order CPU, memory, network. C has an effect only together with A.
- **Audit line**: for every fault, the strict rank, the list position of the first matching
  candidate and the list position of the first candidate on the injected pod. Definitions are in
  `PREREGISTRATION.md`, Section 2.
- **NEZHA_MODALITY** = `all` (default), `noM`, `noL` or `noML`: our reimplementation of the paper's
  modality ablation, which is not shipped in the released code.

## Running

```bash
python3.10 -m venv .venv
./.venv/bin/pip install drain3 matplotlib more_itertools numpy pandas psutil pyyaml tqdm scipy scikit-learn

# Restore pristine Drain3 state before every run: evaluation rewrites these files.
git checkout -- log_template/hipster.bin log_template/ts.bin

./.venv/bin/python main.py --ns hipster --level service                       # original behaviour
NEZHA_ALARM_MODE=AB NEZHA_K=3 ./.venv/bin/python main.py --ns hipster --level service
NEZHA_ALARM_MODE=A NEZHA_ATTRIBUTION=ratio ./.venv/bin/python main.py --ns ts --level service   # A+C
NEZHA_MODALITY=noM ./.venv/bin/python main.py --ns hipster --level service    # without metrics
```

`--ns` is `hipster` (OnlineBoutique) or `ts` (TrainTicket); `--level` is `service` or `inner`.
Results are written to `log/<date>_nezha.log`.

Round 2 as a whole (about 13 hours on one laptop, two runs in parallel):

```bash
bash g22/scripts/run_round2.sh                          # the 22 runs, into g22/logs/round2/
./.venv/bin/python g22/scripts/analyze_round2.py        # writes g22/logs/round2/analysis/
./.venv/bin/python g22/scripts/evaluator_unit_tests.py  # 9 synthetic checks of the rank rules
./.venv/bin/python g22/scripts/threshold_provenance.py  # recomputes the shipped threshold statistics
```

`run_round2.sh` skips every job that already has a folder in `g22/logs/round2/claims/`. Remove that
folder to run a job again.

## Results

### Reproduction: all four configurations match the paper exactly

| System | Level | Paper | Reproduced |
|---|---|---|---|
| OnlineBoutique | service | 92.86 / 96.43 / 96.43 | 92.857143 / 96.428571 / 96.428571 |
| OnlineBoutique | inner-service | 92.86 / 96.43 / 96.43 | 92.857143 / 96.428571 / 96.428571 |
| TrainTicket | service | 86.67 / 97.78 / 97.78 | 86.666667 / 97.777778 / 97.777778 |
| TrainTicket | inner-service | 86.67 / 97.78 / 97.78 | 86.666667 / 97.777778 / 97.777778 |

Values are AS@1 / AS@3 / AS@5 (AIS@k at inner-service level). In all four configurations the
per-case ranks are also identical to the authors' shipped run logs in `log/`. The round-2 baseline
runs (1, 2, 21, 22) repeat the round-1 ranks on every fault.

### Round 1: OnlineBoutique, service level, k = 3

| Variant | AS@1 | AS@5 | Cases changed |
|---|---|---|---|
| baseline | 52/56 | 54/56 | n/a |
| A | 52/56 | 54/56 | 0 |
| B | 51/56 | 53/56 | 5 |
| AB | 51/56 | 53/56 | the same 5 |

B recovers the targeted case (adservice, network_delay) but loses two others. Round-2 runs 18 to 20
repeat these three variants with identical ranks on all 56 faults.

### Round 2: 22 pre-registered runs

All 22 runs finished with exit 0. The full report is
[`logs/round2/analysis/report.md`](logs/round2/analysis/report.md); the per-case table is `percase.csv`
in the same folder.

AS@1 by the released evaluator, service level. Baselines: 52 of 56 (OnlineBoutique) and 39 of 45
(TrainTicket).

| Variant | OnlineBoutique (of 56) | TrainTicket (of 45) |
|---|---|---|
| A | 52 | 39 |
| B, k = 1 | 46 | 6 |
| B, k = 2 | 47 | 2 |
| B, k = 3 | 51 | 17 |
| B, k = 4 | 49 | 36 |
| B, k = 5 | 47 | 36 |
| A+B, k = 3 | 51 | 17 |
| A+C | 49 | 39 |
| A+B+C, k = 3 | 51 | 17 |

- **A changes no rank-1 result** on either system.
- **B is below the baseline at every multiplier on both systems.** On TrainTicket at k = 3 it loses
  22 faults that the baseline gets right and gains none. All 22 are on 2023-01-29.
- **C fails its pre-registered criteria.** Under A+C the targeted adservice fault is diagnosed at
  rank 1, but four OnlineBoutique faults that the baseline gets right are lost (two currencyservice
  and two adservice CPU faults), and AS@1 falls from 52 to 49. On TrainTicket, the held-out system,
  A+C changes nothing (39 to 39).
- **McNemar exact test, 18 tests, no correction:** five are significant (p < 0.001), all on
  TrainTicket: B at k = 1, 2 and 3, A+B and A+B+C. The test has low power at 56 and 45 faults, so the
  other 13 results are not evidence of no effect.

**Evaluator audit.** The released rank rule does not advance the rank counter for a non-matching
candidate that carries a resource, and candidates with tied score and depth share a rank. The
released rank and an audit value disagree in 210 of 1,111 case-runs. Both baselines are unaffected at
rank 1. For B at k = 3 on TrainTicket, AS@5 is 41 of 45 by the released rule and 23 of 45 by list
position; at k = 2 it is 31 against 8.

**Alarms in fault-free minutes.** The original rule raises 2 alarms in the two OnlineBoutique
fault-free minutes and 0 in the two TrainTicket ones. B raises 0 on OnlineBoutique and 22, 14, 8, 6
and 5 on TrainTicket for k = 1 to 5.

**Threshold statistics.** The shipped `metric_threshold/*.csv` means and standard deviations can be
recomputed from the shipped data for 2 of 56 services (both all zero). For the other 54 no shipped
date, or pair of dates, gives the shipped values. See
[`logs/round2/analysis/threshold_provenance.md`](logs/round2/analysis/threshold_provenance.md).

**Deviations from the pre-registration.** The batch was interrupted once and restarted, and three
descriptive checks were added after the data were seen. Both are recorded at the end of
`PREREGISTRATION.md`.

## Main findings

1. **The released code has no anomaly trigger.** Evaluation analyses the minute two minutes after each
   known injection, for every fault.
2. **Alarms use fixed global thresholds** (CPU and memory 80 %, network 200 ms or 300 ms). The k-sigma
   rule is present in `determine_alarm` but commented out.
3. **`generate_alarm` keeps only the first alarming metric per pod.**
4. **Each candidate carries one resource, taken from the first alarm in the order CPU, memory, network.**
   Changing which alarms fire therefore changes which resource is blamed.
5. **Enabling the k-sigma rule (B) lowers accuracy** at every multiplier from 1 to 5, on both systems.
6. **Choosing the resource by relative exceedance (C) does not fix attribution.** A CPU fault can push
   network latency further above its threshold than CPU usage is above its own, so the symptom wins.
7. **The released evaluator can report a higher AS@k than the candidate list supports**, most visibly
   for variants that raise many alarms.
8. **The shipped threshold statistics cannot be rebuilt from the shipped data** for 54 of 56 services.

## Reproducibility notes

- Pinned `numpy==1.15.4` and `pandas==0.23.4` do not build on Python 3.10 or arm64; unpinned versions
  give identical results.
- `tqdm` is imported but missing from `requirements.txt`.
- Running the evaluation rewrites `log_template/*.bin`; restore them before each run.
- One injection time in `rca_data/2022-08-22/2022-08-22-fault_list.json` differs from the authors'
  shipped log (03:53:54 against 03:53:10), in the same minute, with no effect on results.
- The pipeline has no random-number generation. Every configuration that was run twice gave the same
  rank for every fault.
- Runtime is not compared between variants: round-2 runs executed two at a time.
- The `*_time.txt` files of round 2 contain Python warning lines with the local folder path of the
  machine that ran them.

## Contents of `g22/`

| Path | Contents |
|---|---|
| `PREREGISTRATION.md` | Questions, definitions, the 22 runs, analyses and success criteria of round 2, Amendment 1 and the deviations |
| `scripts/` | Run queues, the per-case comparison script, alarm and false-alarm probes, the round-2 analysis, the evaluator unit tests and the threshold check, as used. The run queues assume our local directory layout. |
| `logs/reproduction/` | Our run logs for all four configurations |
| `logs/ablation/` | Round 1: run logs and `/usr/bin/time -l` output for each ablation variant |
| `logs/modality/` | Modality ablation run logs |
| `logs/equivalence/` | Round 1: alarm lists of the current `alarm.py` and of the code used for the A/B runs |
| `logs/round2/` | Round 2: run log, stdout and time output of each of the 22 runs, `round2.log`, alarm-list equivalence files, false-alarm probes and the pristine Drain copies |
| `logs/round2/analysis/` | `report.md`, `percase.csv` and `threshold_provenance.md` |
| `provenance/` | Exact code used for the A/B runs, upstream commit, Drain3 hashes and full resolved environment |
