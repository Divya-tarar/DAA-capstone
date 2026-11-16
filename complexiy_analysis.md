# Algorithm Complexity Analysis
## Mini-Courier Planner

### 1. Merge Sort – Package Prioritization

Merge Sort is used to arrange parcels according to their delivery deadlines.

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Space Complexity: O(n)

Merge Sort was selected because it provides consistent performance for sorting larger datasets.

### 2. 0/1 Knapsack – Package Selection

Dynamic Programming is used to select packages that maximize total value without exceeding the vehicle's weight capacity.

- Time Complexity: O(n × W)
- Space Complexity: O(n × W)

Here, n represents the number of packages and W represents the vehicle capacity.

### 3. Dijkstra's Algorithm – Shortest Path

Dijkstra's Algorithm calculates the shortest distance from the warehouse to different delivery locations.

Using an adjacency list and priority queue:

- Time Complexity: O((V + E) log V)
- Space Complexity: O(V + E)

Here, V represents vertices and E represents edges.

### 4. Nearest Neighbor – Route Planning

The Nearest Neighbor approximation technique selects the closest unvisited delivery location at each step.

- Time Complexity: O(V²)
- Space Complexity: O(V)

It provides a practical approximate route without checking every possible route.

### 5. Bubble Sort vs Merge Sort – Performance Comparison

Bubble Sort and Merge Sort are compared using different dataset sizes.

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Bubble Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |

The performance experiment demonstrates that Merge Sort becomes significantly faster than Bubble Sort as the dataset size increases.

### Conclusion

The project combines sorting, dynamic programming, graph algorithms and approximation techniques to solve a courier-planning problem.

The algorithms were selected according to their suitability for package prioritization, capacity optimization and route calculation. The performance comparison also demonstrates the advantage of efficient sorting algorithms for larger datasets.