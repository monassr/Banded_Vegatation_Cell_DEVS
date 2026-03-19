import json
import random
import sys

NUM_ROWS = 50
NUM_COLS = 50

DENSITY = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5

def generate_random_cell_map(num_rows, num_cols, density):
    
    random.seed(47)  
    cell_map = []
    
    for r in range(num_rows):
        for c in range(num_cols):
            if random.random() < density:
                cell_map.append([r, c])
                
    return cell_map

def build_config(cell_map):
    
    return {
        "scenario": {
            "shape": [NUM_ROWS, NUM_COLS],
            "origin": [0, 0],
            "wrapped": True
        },
        "cells": {
            "default": {
                "delay": "transport",
                "model": "vegetation",
                "state": {"vegetation": False},
                "neighborhood": [
                    {"type": "relative", "neighbors": [[-1, 1], [0, 1], [1, 1]], "vicinity": 2.0},
                    {"type": "relative", "neighbors": [[-1, 0], [1, 0], [0, -1]], "vicinity": 1.0},
                    {"type": "relative", "neighbors": [[-1, 2], [0, 2], [1, 2], [-2, 1], [-2, 0], [2, 1], [2, 0]], "vicinity": 0.5},
                    {"type": "relative", "neighbors": [[0, 0]], "vicinity": 0.0}
                    
                    
                    # {"type": "relative", "neighbors": [[1, -1], [1, 0], [1, 1]], "vicinity": 2.0},
                    # {"type": "relative", "neighbors": [[0, -1], [0, 1], [-1, 0]], "vicinity": 1.0},
                    # {"type": "relative", "neighbors": [[2, -1], [2, 0], [2, 1], [1, -2], [0, -2], [1, 2], [0, 2]], "vicinity": 0.5},
                    # {"type": "relative", "neighbors": [[0, 0]], "vicinity": 0.0}
                ]
            },
            "vegetated": {
                "state": {"vegetation": True},
                "cell_map": cell_map
            }
        },
        "viewer": [
            {
                "colors": [[255, 255, 255], [0, 128, 0]],
                "breaks": [0, 0.5, 1],
                "field": "vegetation"
            }
        ]
    }

if __name__ == "__main__":
    cell_map = generate_random_cell_map(NUM_ROWS, NUM_COLS, DENSITY)
    config = build_config(cell_map)
    print(json.dumps(config, indent=2))
