# Banded Vegetation — Cadmium Cell-DEVS Simulation

A Banded Vegetation spreading model based on the Cell-DEVS formalism and implemented with the [Cadmium v2](https://github.com/Sasisekhar/cadmium_v2) simulation framework in C++.

## Project Structure

```
main [This folder contains the Cell-DEVS model implementation]
    main.cpp
    include/
        vegetationState.hpp
        vegetationCell.hpp
generators [This folder contains Python scripts that generate initial state configurations]
    generate_cell_map_clusters.py
    generate_cell_map_diagonal.py
    generate_cell_map_middle.py
    generate_cell_map_random.py
config [This folder stores the generated JSON configuration file for each scenario ran]
    vegetation_config.json
log [This folder stores the generated output log for each scenario ran]
bin [This folder will be created automatically the first time you compile the project.
     It will contain the executable]
build [This folder will be created automatically the first time you compile the project.
       It will contain all the build files generated during compilation]
run_clusters.sh
run_diagonal.sh
run_middle.sh
run_random.sh
run_scenario.sh
build_sim.sh
CMakeLists.txt
```

## Prerequisites

- [Cadmium v2](https://github.com/Sasisekhar/cadmium_v2) 
- **Python 3** — required to run the generator scripts that produce the initial state configuration files

## Building

Each run script handles the full build-and-run cycle automatically. 

The simplest way to run any scenario is through the provided shell scripts. To ensure the scripts are executable, run the following once:

```bash
chmod +x run_*.sh
```

Each script accepts an **optional** simulation time argument. If not provided, the default is **50** time steps.

### Individual Scenario Scripts

**Clusters** — two vegetation clusters connected by a diagonal bridge:
```bash
./run_clusters.sh [sim_time]
```

**Diagonal** — a single diagonal band with three full vegetated lines:
```bash
./run_diagonal.sh [sim_time]
```

**Middle** — the middle third of the grid fully vegetated:
```bash
./run_middle.sh [sim_time]
```

**Random** — randomly distributed vegetation:
```bash
./run_random.sh [sim_time]
```

For example:

The below runs the clusters scenario for 200 time units:

```bash
./run_clusters.sh 200 
```

The below runs the diagonal scenario for 50 time units since no additional argument was provided
```bash
./run_diagonal.sh
```

## Simulation Output

Each script produces two output files:

| File | Location | Description |
|---|---|---|
| `vegetation_config.json` | `config/` | The generated JSON configuration used for the simulation |
| `grid_log.csv` | `log/` | Semicolon-delimited CSV log with columns: `time;model_id;model_name;port_name;data` |
