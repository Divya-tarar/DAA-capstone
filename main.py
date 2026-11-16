from mini_courier_planner import (
    prioritize_packages,
    knapsack_optimization,
    shortest_path_demo,
    route_planning_demo
)


def main():

    print("=" * 50)
    print("          MINI-COURIER PLANNER")
    print("=" * 50)

    # Sample package dataset
    packages = [
        {"id": "P1", "deadline": 2, "weight": 4, "value": 100, "location": "A"},
        {"id": "P2", "deadline": 5, "weight": 2, "value": 80, "location": "B"},
        {"id": "P3", "deadline": 1, "weight": 6, "value": 150, "location": "C"},
        {"id": "P4", "deadline": 3, "weight": 3, "value": 90, "location": "A"},
        {"id": "P5", "deadline": 4, "weight": 5, "value": 120, "location": "C"}
    ]

    # STEP 1: Package Prioritization
    print("\nSTEP 1: PACKAGE PRIORITIZATION")

    sorted_packages = prioritize_packages(packages)

    # STEP 2: Knapsack Optimization
    print("\nSTEP 2: PACKAGE SELECTION")

    selected_packages = knapsack_optimization(
        sorted_packages, 10
    )

    # STEP 3: Shortest Path using Dijkstra
    print("\nSTEP 3: SHORTEST PATH CALCULATION")

    graph = shortest_path_demo()

    # STEP 4: Courier Route Planning
    print("\nSTEP 4: COURIER ROUTE PLANNING")

    route_planning_demo(selected_packages, graph)

    print("\n" + "=" * 50)
    print("       COURIER PLANNING COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()