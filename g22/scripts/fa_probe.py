"""False-alarm measurement: alarms raised in the four fault-free construction minutes."""
import json, os, sys
import alarm
mins = [("hipster", "2022-08-22 03:51"), ("hipster", "2022-08-23 17:00"),
        ("ts", "2023-01-29 08:50"), ("ts", "2023-01-30 11:39")]
out = {}
for ns, t in mins:
    al = alarm.generate_alarm(alarm.get_metric_with_time(t, "construct_data"), ns)
    out[t] = {"ns": ns, "pods": len(al), "alarms": sum(len(a["alarm"]) for a in al),
              "detail": sorted([(a["pod"].rsplit('-', 2)[0], sorted(x["metric_type"] for x in a["alarm"])) for a in al])}
print(json.dumps({"mode": alarm.ALARM_MODE, "result": out}))
