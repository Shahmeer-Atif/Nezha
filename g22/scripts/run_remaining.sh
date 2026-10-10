#!/usr/bin/env bash
# Reproduce the three remaining Nezha configurations.
# Each run starts from the authors' pristine Drain3 persistence state.
cd "$(dirname "$0")"
OUT=runs
START=$(date +%s)
echo "BATCH START $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee "$OUT/batch.log"

run_one () {
  NS=$1; LEVEL=$2; TAG=$3
  echo "" | tee -a "$OUT/batch.log"
  echo "=== $TAG  (--ns $NS --level $LEVEL)  start $(date -u +%H:%M:%SZ) ===" | tee -a "$OUT/batch.log"
  # restore pristine drain3 state so each run starts from the shipped baseline
  git checkout -- log_template/hipster.bin log_template/ts.bin 2>/dev/null
  # move aside any existing dated log so this run's log is isolated
  for f in log/*_nezha.log; do [ -e "$f" ] && mv "$f" "$OUT/prev_$(basename "$f").$(date +%s)"; done
  T0=$(date +%s)
  ./.venv/bin/python ./main.py --ns "$NS" --level "$LEVEL" > "$OUT/${TAG}_stdout.txt" 2>&1
  RC=$?
  T1=$(date +%s)
  for f in log/*_nezha.log; do [ -e "$f" ] && cp "$f" "$OUT/${TAG}_nezha.log"; done
  echo "    exit=$RC  duration=$(( (T1-T0)/60 ))m$(( (T1-T0)%60 ))s" | tee -a "$OUT/batch.log"
  grep -A1 -E "S@1 Result|S@3 Result|S@5 Result|Fault numbuer" "$OUT/${TAG}_nezha.log" 2>/dev/null \
    | grep -oE "[0-9]+\.[0-9]+ %|Fault numbuer : [0-9]+" | tr '\n' ' ' | tee -a "$OUT/batch.log"
  echo "" | tee -a "$OUT/batch.log"
}

run_one hipster inner  OnlineBoutique_inner
run_one ts      service TrainTicket_service
run_one ts      inner   TrainTicket_inner

git checkout -- log_template/hipster.bin log_template/ts.bin 2>/dev/null
echo "" | tee -a "$OUT/batch.log"
echo "BATCH DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)  total=$(( ($(date +%s)-START)/60 )) min" | tee -a "$OUT/batch.log"
