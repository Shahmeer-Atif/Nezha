import sys, json, importlib
mod = importlib.import_module(sys.argv[1])
cases = [("hipster","2022-08-23 14:32"),("hipster","2022-08-23 16:07"),("ts","2023-01-30 13:32"),
         ("hipster","2022-08-22 04:29"),("hipster","2022-08-23 12:37"),("ts","2023-01-30 11:53")]
out = {}
for ns, t in cases:
    ml = mod.get_metric_with_time(t, "rca_data")
    al = mod.generate_alarm(ml, ns)
    out[t] = sorted([(a["pod"].rsplit('-',2)[0], sorted(x["metric_type"] for x in a["alarm"])) for a in al])
print(json.dumps(out))
