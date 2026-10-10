# G22: Reproduction and Alarm-Stage Study of Nezha

This branch extends [Nezha](https://github.com/IntelligentDDS/Nezha) (Yu et al., ESEC/FSE 2023) for a
research assignment in Cloud Computing at FAST NUCES Islamabad.

**Authors:** Shahmeer Atif (23i-0711) and Taaha Zaman Khan (22i-1377), Group G22.
**Licence:** the original MIT licence and copyright notice are retained. All credit for Nezha belongs to its authors.

## What changed

Only two files are modified. With no environment variables set, behaviour is identical to the original.

| File | Change |
|---|---|
| `alarm.py` | `NEZHA_ALARM_MODE` = `baseline` (default), `A`, `B` or `AB`; `NEZHA_K` (default 3); `NEZHA_MODALITY` metric switch |
| `data_integrate.py` | `NEZHA_MODALITY` log switch |

- **A**: `generate_alarm` keeps every alarming metric per pod. The original keeps only the first.
- **B**: CPU and memory alarms use per-service `mean + k * std` from `metric_threshold/<service>.csv`,
  instead of a fixed 80 %. Falls back to 80 % where no usable baseline exists.
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
NEZHA_MODALITY=noM ./.venv/bin/python main.py --ns hipster --level service    # without metrics
```

`--ns` is `hipster` (OnlineBoutique) or `ts` (TrainTicket); `--level` is `service` or `inner`.
Results are written to `log/<date>_nezha.log`.

## Results

### Reproduction: all four configurations match the paper exactly

| System | Level | Paper | Reproduced |
|---|---|---|---|
| OnlineBoutique | service | 92.86 / 96.43 / 96.43 | 92.857143 / 96.428571 / 96.428571 |
| OnlineBoutique | inner-service | 92.86 / 96.43 / 96.43 | 92.857143 / 96.428571 / 96.428571 |
| TrainTicket | service | 86.67 / 97.78 / 97.78 | 86.666667 / 97.777778 / 97.777778 |
| TrainTicket | inner-service | 86.67 / 97.78 / 97.78 | 86.666667 / 97.777778 / 97.777778 |

Values are AS@1 / AS@3 / AS@5 (AIS@k at inner-service level). For OnlineBoutique at service level,
all 56 per-case ranks are also identical to the authors' shipped run log.

### Ablation: OnlineBoutique, service level, k = 3

| Variant | AS@1 | AS@5 | Cases changed |
|---|---|---|---|
| baseline | 52/56 | 54/56 | n/a |
| A | 52/56 | 54/56 | 0 |
| B | 51/56 | 53/56 | 5 |
| AB | 51/56 | 53/56 | the same 5 |

B recovers the targeted case (adservice, network_delay) but loses two others. **The improvement as
designed does not raise accuracy.**

## Main findings

1. **The released code has no anomaly trigger.** Evaluation analyses the minute two minutes after each
   known injection, for every fault.
2. **Alarms use fixed global thresholds** (CPU and memory 80 %, network 200 ms or 300 ms). The k-sigma
   rule is present in `determine_alarm` but commented out.
3. **`generate_alarm` keeps only the first alarming metric per pod.**
4. **Each candidate carries one resource, taken from the first alarm in the order CPU, memory, network.**
   Changing which alarms fire therefore changes which resource is blamed. This explains every case
   changed by the ablation, and is the stage a next component should target.

## Reproducibility notes

- Pinned `numpy==1.15.4` and `pandas==0.23.4` do not build on Python 3.10 or arm64; unpinned versions
  give identical results.
- `tqdm` is imported but missing from `requirements.txt`.
- Running the evaluation rewrites `log_template/*.bin`; restore them before each run.
- One injection time in `rca_data/2022-08-22/2022-08-22-fault_list.json` differs from the authors'
  shipped log (03:53:54 against 03:53:10), in the same minute, with no effect on results.

## Contents of `g22/`

| Path | Contents |
|---|---|
| `scripts/` | Run queues, the per-case comparison script, and alarm and false-alarm probes, as used. They assume our local directory layout. |
| `logs/reproduction/` | Our run logs for all four configurations |
| `logs/ablation/` | Run logs and `/usr/bin/time -l` output for each ablation variant |
| `logs/modality/` | Modality ablation run logs |
| `provenance/` | Exact code used for the A/B runs, upstream commit, Drain3 hashes and full resolved environment |
