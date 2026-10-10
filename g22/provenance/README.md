# Provenance

| Item | Value |
|---|---|
| Upstream commit used for all four reproduction runs | `d8140101fdb4e7dfb60d3ef9f64706f382b68470` (IntelligentDDS/Nezha) |
| Code used for the A, B and A+B runs | upstream commit above, with `alarm.py` replaced by `alarm_as_tested_for_AB_runs.py` in this folder; `data_integrate.py` unmodified |
| Difference from the branch tip | the branch tip additionally adds the `NEZHA_MODALITY` switch (default `all`, off) to `alarm.py` and `data_integrate.py`; with defaults the alarm and log paths are unchanged |
| Pristine Drain3 state | `drain3-pristine-sha256.txt`; restored before every run |
| Python | 3.10.21 on macOS 27.0, arm64 |
| Full resolved environment | `requirements-resolved.txt` (`pip freeze`, 26 packages) |
