
def merge_sort(packages):
    if len(packages) <= 1:
        return packages

    mid = len(packages) // 2

    left = merge_sort(packages[:mid])
    right = merge_sort(packages[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["deadline"] <= right[j]["deadline"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def prioritize_packages(packages):

    sorted_packages = merge_sort(packages)

    print("\n=== Package Prioritization ===")
    print("Sorted by earliest delivery deadline:\n")

    for package in sorted_packages:
        print(
            f"Parcel: {package['id']} | "
            f"Deadline: {package['deadline']} hours | "
            f"Weight: {package['weight']} kg | "
            f"Value: {package['value']}"
        )

    return sorted_packages

def knapsack_optimization(packages, capacity):
    n = len(packages)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        weight = packages[i - 1]["weight"]
        value = packages[i - 1]["value"]

        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(
                    value + dp[i - 1][w - weight],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected packages
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(packages[i - 1])
            w -= packages[i - 1]["weight"]

    selected.reverse()

    print("\n=== Knapsack Optimization ===")
    print("Vehicle capacity:", capacity, "kg")
    print("Selected parcels:")

    total_weight = 0

    for package in selected:
        print(
            f"Parcel: {package['id']} | "
            f"Weight: {package['weight']} kg | "
            f"Value: {package['value']}"
        )
        total_weight += package["weight"]

    print("Total weight:", total_weight, "kg")
    print("Maximum total value:", dp[n][capacity])
    return selected 


import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances


def shortest_path_demo():
    graph = {
        "Warehouse": [("A", 4), ("B", 2)],
        "A": [("Warehouse", 4), ("B", 1), ("C", 5)],
        "B": [("Warehouse", 2), ("A", 1), ("C", 8), ("D", 10)],
        "C": [("A", 5), ("B", 8), ("D", 2)],
        "D": [("B", 10), ("C", 2)]
    }

    distances = dijkstra(graph, "Warehouse")

    print("\n=== Shortest Path Using Dijkstra ===")

    for location, distance in distances.items():
        print(f"Warehouse to {location}: {distance} km")
    return graph 

def nearest_neighbor_route(distances, start):
    unvisited = set(distances.keys())
    unvisited.remove(start)

    route = [start]
    current = start
    total_distance = 0

    while unvisited:
        next_location = min(
            unvisited,
            key=lambda location: distances[current][location]
        )

        total_distance += distances[current][next_location]
        route.append(next_location)
        unvisited.remove(next_location)
        current = next_location

    total_distance += distances[current][start]
    route.append(start)

    return route, total_distance


def route_planning_demo(selected_packages, graph):

    delivery_locations = list(
        dict.fromkeys(
            package["location"]
            for package in selected_packages
        )
    )

    locations = ["Warehouse"] + delivery_locations

    # Calculate shortest distances between all required locations
    distance_matrix = {}

    for location in locations:
        all_distances = dijkstra(graph, location)

        distance_matrix[location] = {
            other: all_distances[other]
            for other in locations
            if other != location
        }

    # Generate delivery route
    route, total_distance = nearest_neighbor_route(
        distance_matrix,
        "Warehouse"
    )

    print("\n=== Courier Route Planning ===")

    print("Selected package locations:")

    for package in selected_packages:
        print(package["id"], "->", package["location"])

    print("\nDelivery Route:", " -> ".join(route))
    print("Total Route Distance:", total_distance, "km")



if __name__ == "__main__":
    packages = [
        {"id": "P1", "deadline": 2, "weight": 4, "value": 100},
        {"id": "P2", "deadline": 5, "weight": 2, "value": 80},
        {"id": "P3", "deadline": 1, "weight": 6, "value": 150},
        {"id": "P4", "deadline": 3, "weight": 3, "value": 90},
        {"id": "P5", "deadline": 4, "weight": 5, "value": 120}
    ]

    prioritize_packages()
    knapsack_optimization(packages, 10)
    shortest_path_demo()
    route_planning_demo()



