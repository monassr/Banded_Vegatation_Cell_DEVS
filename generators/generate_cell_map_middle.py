import json

NUM_ROWS = 50
NUM_COLS = 50

def generate_rows():
    rows = []
    third = NUM_COLS//3
    start_col = third          
    end_col = third*2        
    
    for r in range(NUM_ROWS):
        row = ['0']*NUM_COLS
        for c in range(start_col, end_col):
            row[c] = '1'
        rows.append(''.join(row))
        
    return rows

ROWS = generate_rows()

def generate_cell_map(rows):

    cell_map = []
    
    for r, row_str in enumerate(rows):
        for c, ch in enumerate(row_str):
            if ch == '1':
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
    cell_map = generate_cell_map(ROWS)
    config = build_config(cell_map)
    print(json.dumps(config, indent=2))
