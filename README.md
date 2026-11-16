# Mini-Courier Planner

## Project Overview

Mini-Courier Planner is a Python-based project developed as part of the Design and Analysis of Algorithms (DAA) Capstone Assignment.

The project simulates an intelligent courier planning system that prioritizes parcels, optimizes package selection based on vehicle capacity, calculates shortest delivery paths and generates an approximate delivery route.

It combines sorting, dynamic programming, graph algorithms and approximation techniques.

## Objectives

- Prioritize parcels according to delivery deadlines.
- Select the most valuable combination of parcels within vehicle capacity.
- Calculate shortest paths between delivery locations.
- Generate an efficient approximate courier route.
- Compare the execution time of different sorting algorithms.

## Algorithms Used

| Algorithm | Application |
|---|---|
| Merge Sort | Parcel prioritization |
| 0/1 Knapsack | Package selection |
| Dijkstra's Algorithm | Shortest path calculation |
| Nearest Neighbor | Courier route planning |
| Bubble Sort | Performance comparison |

## Technologies Used

- Python
- VS Code
- Matplotlib
- CSV
- Git and GitHub

## Project Structure

```text
DAA Capstone/
│
├── main.py
├── mini_courier_planner.py
├── performance_testing.py
├── complexity_analysis.md
├── README.md
│
├── datasets/
│
├── results/
│   ├── performance_comparison.png
│   └── performance_results.csv
│
├── screenshots/
│
└── docs/
    └── Mini_Courier_Planner_Report.md
```

## How to Run the Project

### Requirements

Python 3 and Matplotlib are required.

Install Matplotlib using:

```bash
pip install matplotlib
```

### Run the Main Application

Open the project folder in VS Code and execute:

```bash
python main.py
```

### Run Performance Testing

Execute:

```bash
python performance_testing.py
```

## Sample Results

The sample application demonstrates:

- Packages sorted by delivery deadline.
- Optimal package selection within a 10 kg vehicle capacity.
- Maximum selected package value of 290.
- Shortest paths calculated using Dijkstra's Algorithm.
- Approximate delivery route:

Warehouse → B → A → C → Warehouse

- Total route distance: 16 km.

## Performance Analysis

Bubble Sort and Merge Sort are compared using different dataset sizes.

The execution times are recorded in a CSV file, and a graphical comparison is generated to demonstrate their performance differences.

The results show that Merge Sort performs more efficiently than Bubble Sort as the input size increases.

## Complexity Analysis

Detailed time and space complexity analysis of the implemented algorithms is available in:

`complexity_analysis.md`

## Project Evidence

The `screenshots` folder contains execution screenshots demonstrating the integrated application and its output.

The `results` folder contains the performance comparison graph and CSV data.

## Conclusion

The Mini-Courier Planner demonstrates how different algorithmic techniques can be integrated to solve a practical courier-planning problem.

It provides an understanding of algorithm selection, optimization, computational complexity and performance evaluation.

## Future Scope

- Use real-world geographical coordinates.
- Include additional delivery locations and parcel datasets.
- Implement more advanced route optimization techniques.
- Develop a graphical user interface.
- Support real-time delivery tracking.