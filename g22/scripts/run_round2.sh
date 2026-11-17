#!/usr/bin/env bash
# G22 round-2 runs, as pre-registered in g22/PREREGISTRATION.md.
# Start from anywhere:   bash g22/scripts/run_round2.sh
# Two workers run jobs in parallel, each in its own directory, because every run rewrites the
# Drain files in log_template/ and writes log/<date>_nezha.log.
# Results go to g22/logs/round2/. Progress: tail -f g22/logs/round2/round2.log
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
WORK="$(cd "$REPO/.." && pwd)/nezha-workers"
RES="$REPO/g22/logs/round2"
JOBS="$RES/jobs.txt"
LOG="$RES/round2.log"
mkdir -p "$RES/claims" "$RES/pristine" "$RES/equivalence" "$WORK"

# ---- pristine Drain state, verified against the recorded hashes ----
cp "$REPO/log_template/hipster.bin" "$RES/pristine/hipster.bin"
cp "$REPO/log_template/ts.bin" "$RES/pristine/ts.bin"
for f in hipster ts; do
  want=$(grep " $f.bin" "$REPO/g22/provenance/drain3-pristine-sha256.txt" | awk '{print $1}')
  got=$(shasum -a 256 "$RES/pristine/$f.bin" | awk '{print $1}')
  [ "$want" = "$got" ] || { echo "ABORT: $f.bin is not pristine ($got)" | tee -a "$LOG"; exit 1; }
done

# ---- worker directories: own code, Drain files and log dir; shared read-only data ----
for w in w1 w2; do
  D="$WORK/$w"; rm -rf "$D"; mkdir -p "$D/log" "$D/log_template"
  cp "$REPO"/*.py "$D/"
  cp "$REPO"/log_template/* "$D/log_template/"
  for l in rca_data construct_data metric_threshold .venv; do ln -s "$REPO/$l" "$D/$l"; done
done
PY="./.venv/bin/python"

echo "ROUND2 START $(date -u +%Y-%m-%dT%H:%M:%SZ) commit=$(git -C "$REPO" rev-parse --short HEAD)" | tee -a "$LOG"

# ---- step 0: alarm equivalence for the k values not checked earlier, and false-alarm counts ----
cp "$REPO/g22/provenance/alarm_as_tested_for_AB_runs.py" "$WORK/w1/alarm_as_tested.py"
cp "$REPO/g22/scripts/fa_probe.py" "$WORK/w1/fa_probe.py"   # imports alarm.py from its own directory
( cd "$WORK/w1"
  for k in 1 2 4 5; do for impl in alarm alarm_as_tested; do
    NEZHA_ALARM_MODE=B NEZHA_K=$k nice -n 5 $PY "$REPO/g22/scripts/alarm_equivalence.py" $impl \
      > "$RES/equivalence/B_k${k}_${impl}.json" 2>/dev/null &
  done; done; wait )
for k in 1 2 4 5; do
  if cmp -s "$RES/equivalence/B_k${k}_alarm.json" "$RES/equivalence/B_k${k}_alarm_as_tested.json"; then r=IDENTICAL; else r=DIFFERENT; fi
  echo "equivalence B k=$k: $r" | tee -a "$LOG"
done
( cd "$WORK/w1"
  for spec in baseline:3 A:3 B:1 B:2 B:3 B:4 B:5 AB:3; do
    NEZHA_ALARM_MODE=${spec%%:*} NEZHA_K=${spec##*:} $PY ./fa_probe.py > "$RES/fa_${spec%%:*}_k${spec##*:}.json" 2>/dev/null
  done )
echo "false-alarm probes written" | tee -a "$LOG"

# ---- job list: tag ns level mode k attribution (priority order, from PREREGISTRATION.md) ----
cat > "$JOBS" <<'EOF'
01_hipster_service_baseline hipster service baseline 3 first
02_ts_service_baseline ts service baseline 3 first
03_hipster_service_A_ratio hipster service A 3 ratio
04_ts_service_A_ratio ts service A 3 ratio
05_hipster_service_AB_k3_ratio hipster service AB 3 ratio
06_ts_service_AB_k3_ratio ts service AB 3 ratio
07_ts_service_A ts service A 3 first
08_ts_service_B_k3 ts service B 3 first
09_ts_service_AB_k3 ts service AB 3 first
10_hipster_service_B_k1 hipster service B 1 first
11_hipster_service_B_k2 hipster service B 2 first
12_hipster_service_B_k4 hipster service B 4 first
13_hipster_service_B_k5 hipster service B 5 first
14_ts_service_B_k1 ts service B 1 first
15_ts_service_B_k2 ts service B 2 first
16_ts_service_B_k4 ts service B 4 first
17_ts_service_B_k5 ts service B 5 first
18_hipster_service_A hipster service A 3 first
19_hipster_service_B_k3 hipster service B 3 first
20_hipster_service_AB_k3 hipster service AB 3 first
21_ts_inner_baseline ts inner baseline 3 first
22_hipster_inner_baseline hipster inner baseline 3 first
EOF

worker () {
  local D="$WORK/$1"
  while read -r TAG NS LEVEL MODE K ATTR; do
    [ -z "$TAG" ] && continue
    mkdir "$RES/claims/$TAG" 2>/dev/null || continue   # atomic claim; the other worker took it
    cd "$D"
    cp "$RES/pristine/hipster.bin" log_template/hipster.bin
    cp "$RES/pristine/ts.bin" log_template/ts.bin
    rm -f log/*_nezha.log
    echo "=== $TAG start $(date -u +%H:%M:%SZ) on $1 ===" >> "$LOG"
    T0=$(date +%s)
    NEZHA_ALARM_MODE=$MODE NEZHA_K=$K NEZHA_ATTRIBUTION=$ATTR /usr/bin/time -l $PY ./main.py --ns "$NS" --level "$LEVEL" \
      > "$RES/${TAG}_stdout.txt" 2> "$RES/${TAG}_time.txt"
    RC=$?; T1=$(date +%s)
    cp log/*_nezha.log "$RES/${TAG}_nezha.log" 2>/dev/null
    ACC=$(grep -A1 -E "S@1 Result|S@3 Result|S@5 Result" "$RES/${TAG}_nezha.log" 2>/dev/null | grep -oE "[0-9]+\.[0-9]+ %" | tr '\n' ' ')
    echo "    $TAG exit=$RC duration=$(( (T1-T0)/60 ))m$(( (T1-T0)%60 ))s  @1/@3/@5: $ACC" >> "$LOG"
  done < "$JOBS"
}
worker w1 & sleep 5; worker w2 &
wait
echo "ROUND2 DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
