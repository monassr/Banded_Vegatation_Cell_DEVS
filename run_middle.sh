cd "$(dirname "$0")" || exit 1

SIM_TIME="${1:-50}"
SCENARIO="middle"
GENERATOR="generators/generate_cell_map_${SCENARIO}.py"
CONFIG="config/vegetation_config.json"
LOG_FILE="log/grid_log.csv"

mkdir -p log

# generate config
echo "Generating config for ${SCENARIO}..."
python3 "$GENERATOR" > "$CONFIG"

# Build
echo "Building..."
bash build_sim.sh

#  run
echo "Running simulation (${SIM_TIME} time steps)..."
./bin/vegetation "$CONFIG" "$SIM_TIME" 

echo "Config:  $CONFIG"
echo "Log:     $LOG_FILE"
