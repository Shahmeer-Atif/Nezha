"""Alarm-list equivalence check between two alarm implementations.

Usage (from the repository root, so that rca_data/ and metric_threshold/ resolve):
    NEZHA_ALARM_MODE=AB NEZHA_K=3 python g22/scripts/alarm_equivalence.py <module_name> > out.json

<module_name> is imported after the environment is set, e.g. "alarm" (current code) or
"alarm_as_tested" (a copy of g22/provenance/alarm_as_tested_for_AB_runs.py placed on the path).
For every analysed minute (fault injection time + 2 min, as in evaluation_pod) and every
fault-free construction minute of both systems, it prints the ordered alarm list per pod:
[(pod, [metric_type, ...]), ...]. Order is kept because the original attribution uses the
first alarm. Two implementations are equivalent for a mode if the JSON outputs are identical.
"""
import datetime
import importlib
import json
import os
import sys

sys.path.insert(0, os.getcwd())
mod = importlib.import_module(sys.argv[1])

SYSTEMS = {
    "hipster": [("2022-08-22", "2022-08-22 03:51"), ("2022-08-23", "2022-08-23 17:00")],
    "ts": [("2023-01-29", "2023-01-29 08:50"), ("2023-01-30", "2023-01-30 11:39")],
}


def minutes():
    for ns, days in SYSTEMS.items():
        for day, normal in days:
            yield ns, normal, "construct_data"
            with open(os.path.join("rca_data", day, day + "-fault_list.json")) as f:
                faults = json.load(f)
            items = faults.values() if isinstance(faults, dict) else faults
            for group in items:
                for fault in (group if isinstance(group, list) else [group]):
                    t = datetime.datetime.strptime(fault["inject_time"], "%Y-%m-%d %H:%M:%S")
                    yield ns, (t + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M"), "rca_data"


out = {}
for ns, minute, base in minutes():
    alarms = mod.generate_alarm(mod.get_metric_with_time(minute, base), ns)
    out[f"{ns} {minute} {base}"] = [(a["pod"], [x["metric_type"] for x in a["alarm"]]) for a in alarms]
print(json.dumps({"mode": os.environ.get("NEZHA_ALARM_MODE", "baseline"),
                  "k": os.environ.get("NEZHA_K", "3"), "windows": len(out), "alarms": out}, sort_keys=True))
