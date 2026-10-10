#!/usr/bin/env bash
# Ablation queue for the G22 alarm-stage improvement.
# Waits for the baseline reproduction batch to finish, so runs do not compete for CPU.
cd "$(dirname "$0")"
BATCH_LOG="../nezha/runs/batch.log"
echo "waiting for baseline batch to finish..."
until grep -q "BATCH DONE" "$BATCH_LOG" 2>/dev/null; do sleep 60; done
OUT=runs; LOG="$OUT/ablation.log"
echo "ABLATION START $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee "$LOG"
run () {
  MODE=$1; K=$2; NS=$3; TAG="${MODE}_k${K}_${NS}_service"
  cp "$OUT/pristine_hipster.bin" log_template/hipster.bin
  cp "$OUT/pristine_ts.bin"      log_template/ts.bin
  rm -f log/*_nezha.log
  echo "=== $TAG start $(date -u +%H:%M:%SZ) ===" | tee -a "$LOG"
  T0=$(date +%s)
  NEZHA_ALARM_MODE=$MODE NEZHA_K=$K /usr/bin/time -l ./.venv/bin/python ./main.py --ns "$NS" --level service \
      > "$OUT/${TAG}_stdout.txt" 2> "$OUT/${TAG}_time.txt"
  RC=$?; T1=$(date +%s)
  cp log/*_nezha.log "$OUT/${TAG}_nezha.log" 2>/dev/null
  RSS=$(grep "maximum resident set size" "$OUT/${TAG}_time.txt" | awk '{printf "%.0f MB", $1/1048576}')
  RES=$(grep -A1 -E "S@1 Result|S@3 Result|S@5 Result" "$OUT/${TAG}_nezha.log" 2>/dev/null | grep -oE "[0-9]+\.[0-9]+ %" | tr '\n' ' ')
  echo "    exit=$RC duration=$(( (T1-T0)/60 ))m$(( (T1-T0)%60 ))s peakRSS=$RSS  @1/@3/@5: $RES" | tee -a "$LOG"
}
run AB       3 hipster
run A        3 hipster
run B        3 hipster
run baseline 3 hipster
run AB       2 hipster
run AB       4 hipster
run AB       3 ts
run A        3 ts
run B        3 ts
cp "$OUT/pristine_hipster.bin" log_template/hipster.bin; cp "$OUT/pristine_ts.bin" log_template/ts.bin
echo "ABLATION DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
