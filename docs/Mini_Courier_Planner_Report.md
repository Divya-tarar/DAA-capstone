# MINI-COURIER PLANNER
## Design and Analysis of Algorithms — Capstone Project

**Submitted by:** Divya  
**Course:** B.Tech CSE (AI/ML)  
**University:** KR Mangalam University  
**Academic Session:** 2026

---

# 1. Abstract

The Mini-Courier Planner is a Python-based application developed to simulate an intelligent courier planning system. The project combines different algorithmic techniques to prioritize parcels, optimize package selection, calculate shortest delivery paths and generate an approximate delivery route.

The system uses Merge Sort for parcel prioritization, Dynamic Programming through the 0/1 Knapsack algorithm for package selection, Dijkstra's Algorithm for shortest path calculation and the Nearest Neighbor technique for route planning.

The project also compares Bubble Sort and Merge Sort to evaluate their execution-time performance for different input sizes.

# 2. Introduction

Courier services involve several computational challenges, including deciding which parcels should be delivered first, selecting packages within vehicle capacity and finding efficient routes between delivery locations.

The Mini-Courier Planner addresses these challenges by integrating multiple algorithms into one application.

The project demonstrates how concepts from Design and Analysis of Algorithms can be applied to a practical problem.

# 3. Problem Statement

To develop a prototype courier planning system that:

- Prioritizes parcels according to delivery deadlines.
- Selects valuable packages within a fixed vehicle capacity.
- Calculates shortest paths between delivery locations.
- Generates an approximate delivery route.
- Evaluates algorithm performance using execution time.

# 4. Objectives

1. Implement an efficient sorting algorithm for parcel prioritization.
2. Apply Dynamic Programming to optimize package selection.
3. Use graph algorithms to calculate shortest paths.
4. Apply an approximation technique for route planning.
5. Compare sorting algorithm performance.
6. Analyse time and space complexity.

# 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| VS Code | Coding environment |
| Matplotlib | Performance visualization |
| CSV | Storing performance measurements |
| Git and GitHub | Version control and project submission |

# 6. System Design

The application consists of four major processing stages.

### Stage 1: Package Prioritization

The package dataset contains:
- Package ID
- Delivery deadline
- Weight
- Value
- Delivery location

Merge Sort arranges packages according to their delivery deadlines.

### Stage 2: Package Selection

The 0/1 Knapsack algorithm selects packages to maximize total value without exceeding the vehicle's weight capacity.

The sample vehicle capacity is 10 kg.

### Stage 3: Shortest Path Calculation

The delivery network is represented as a weighted graph.

Dijkstra's Algorithm calculates the shortest distances from the warehouse to the other locations.

### Stage 4: Courier Route Planning

The Nearest Neighbor approximation technique selects the closest unvisited delivery location at each step and returns to the warehouse.

# 7. Methodology and Algorithms

## 7.1 Merge Sort

Merge Sort is used to prioritize parcels according to their delivery deadlines.

It follows the divide-and-conquer approach:
1. Divide the package list into smaller parts.
2. Recursively sort the smaller parts.
3. Merge the sorted parts.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Space Complexity: O(n)

## 7.2 0/1 Knapsack Using Dynamic Programming

The Knapsack algorithm determines which packages provide the maximum total value without exceeding the vehicle capacity.

Each package can either be selected or rejected.

The algorithm constructs a DP table using package weights and values, then backtracks to identify the selected packages.

Time Complexity: O(n × W)

Space Complexity: O(n × W)

Where:
- n = Number of packages
- W = Vehicle capacity

## 7.3 Dijkstra's Algorithm

Dijkstra's Algorithm calculates the shortest paths from a starting vertex to other vertices in a weighted graph with non-negative edge weights.

The project uses an adjacency-list graph representation and a priority queue.

Time Complexity: O((V + E) log V)

Space Complexity: O(V + E)

Where:
- V = Number of vertices
- E = Number of edges

## 7.4 Nearest Neighbor Approximation

The Nearest Neighbor technique is used to generate an approximate delivery route.

It repeatedly selects the nearest unvisited location until all required locations have been visited. Finally, it returns to the warehouse.

Time Complexity: O(V²)

Space Complexity: O(V)

This method provides a practical approximate route but does not guarantee the globally optimal TSP solution.

# 8. Implementation

The project is implemented using modular Python files.

| File | Description |
|---|---|
| main.py | Main application and integration |
| mini_courier_planner.py | Sorting, Knapsack, Dijkstra and route-planning functions |
| performance_testing.py | Sorting performance comparison |
| README.md | Project instructions |
| complexity_analysis.md | Complexity analysis |

The application is executed using:

`python main.py`

# 9. Results and Observations

The sample application produces the following results.

### 9.1 Package Prioritization

Packages are arranged according to their delivery deadlines using Merge Sort.

### 9.2 Package Selection

For a vehicle capacity of 10 kg, the selected packages are:

| Package | Weight | Value |
|---|---:|---:|
| P2 | 2 kg | 80 |
| P4 | 3 kg | 90 |
| P5 | 5 kg | 120 |
| **Total** | **10 kg** | **290** |

The selected package combination provides a total value of 290 without exceeding the vehicle capacity.

### 9.3 Shortest Path Results

Dijkstra's Algorithm calculates shortest distances from the warehouse.

The sample output is:

| Location | Shortest Distance |
|---|---:|
| Warehouse | 0 km |
| A | 3 km |
| B | 2 km |
| C | 8 km |
| D | 10 km |

### 9.4 Final Delivery Route

The approximate delivery route generated by the application is:

**Warehouse → B → A → C → Warehouse**

Total route distance: **16 km**

# 10. Performance Testing

The project compares Bubble Sort and Merge Sort using different dataset sizes.

The experiment uses input sizes of 100, 500, 1000 and 2000 elements.

The execution time is recorded in:

`results/performance_results.csv`

A graphical comparison is generated and saved as:

`results/performance_comparison.png`

### Performance Observations

- Bubble Sort has quadratic time complexity.
- Merge Sort has O(n log n) time complexity.
- Merge Sort performs more efficiently as the input size increases.
- The performance graph demonstrates the difference between the two algorithms.

Execution times depend on the system and the particular test run.

# 11. Complexity Analysis Summary

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Merge Sort | O(n log n) | O(n) |
| 0/1 Knapsack | O(n × W) | O(n × W) |
| Dijkstra | O((V + E) log V) | O(V + E) |
| Nearest Neighbor | O(V²) | O(V) |
| Bubble Sort | O(n²) | O(1) |

# 12. Limitations

- The application currently uses sample package data.
- Delivery locations are represented using a predefined graph.
- The Nearest Neighbor technique does not guarantee an optimal route.
- The current system does not use real-time traffic or geographical data.
- Performance results depend on the execution environment.

# 13. Future Scope

The project can be extended by:

1. Integrating real-world maps and geographical coordinates.
2. Adding real-time traffic information.
3. Supporting larger parcel datasets.
4. Implementing advanced route optimization techniques.
5. Developing a graphical user interface.
6. Adding real-time delivery tracking.

# 14. Conclusion

The Mini-Courier Planner successfully demonstrates the integration of multiple algorithmic techniques into a single courier-planning application.

Merge Sort is used for parcel prioritization, Dynamic Programming optimizes package selection, Dijkstra's Algorithm calculates shortest paths and the Nearest Neighbor technique generates an approximate delivery route.

The performance comparison between Bubble Sort and Merge Sort demonstrates the importance of selecting efficient algorithms for larger datasets.

Overall, the project provides practical experience in algorithm implementation, optimization, performance evaluation and modular Python development.

# 15. References

1. Course materials and laboratory assignments for Design and Analysis of Algorithms.
2. Python Documentation.
3. Matplotlib Documentation.
4. Algorithm concepts covered during classroom lectures.