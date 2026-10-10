#!/usr/bin/env bash
cd "$(dirname "$0")"
Q1="../nezha-improved/runs/ablation.log"
until [ "$(grep -c 'exit=' "$Q1" 2>/dev/null)" -ge 4 ]; do sleep 60; done
OUT=runs; LOG="$OUT/modality.log"
echo "QUEUE2 START $(date -u +%Y-%m-%dT%H:%M:%SZ) (concurrent with remaining queue-1 runs)" | tee "$LOG"
for m in baseline A B AB; do
  NEZHA_ALARM_MODE=$m ./.venv/bin/python fa_probe.py > "$OUT/fa_$m.json" 2>/dev/null
  echo "false-alarm probe $m: $(python3 -c "import json;d=json.load(open('$OUT/fa_$m.json'))['result'];print({k:(v['pods'],v['alarms']) for k,v in d.items()})")" | tee -a "$LOG"
done
run () {
  MOD=$1; NS=$2; TAG="${MOD}_${NS}_service"
  cp "$OUT/pristine_hipster.bin" log_template/hipster.bin; cp "$OUT/pristine_ts.bin" log_template/ts.bin
  rm -f log/*_nezha.log
  echo "=== $TAG start $(date -u +%H:%M:%SZ) ===" | tee -a "$LOG"
  T0=$(date +%s)
  NEZHA_MODALITY=$MOD /usr/bin/time -l ./.venv/bin/python ./main.py --ns "$NS" --level service > "$OUT/${TAG}_stdout.txt" 2> "$OUT/${TAG}_time.txt"
  RC=$?; T1=$(date +%s)
  cp log/*_nezha.log "$OUT/${TAG}_nezha.log" 2>/dev/null
  RSS=$(grep "maximum resident set size" "$OUT/${TAG}_time.txt" | awk '{printf "%.0f MB", $1/1048576}')
  RES=$(grep -A1 -E "S@1 Result|S@3 Result|S@5 Result" "$OUT/${TAG}_nezha.log" 2>/dev/null | grep -oE "[0-9]+\.[0-9]+ %" | tr '\n' ' ')
  echo "    exit=$RC duration=$(( (T1-T0)/60 ))m$(( (T1-T0)%60 ))s peakRSS=$RSS  @1/@3/@5: $RES" | tee -a "$LOG"
}
run noM hipster
run noL hipster
run noM ts
run noL ts
cp "$OUT/pristine_hipster.bin" log_template/hipster.bin; cp "$OUT/pristine_ts.bin" log_template/ts.bin
echo "QUEUE2 DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
