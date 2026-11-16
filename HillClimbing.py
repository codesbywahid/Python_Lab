# Hill Climbing: Attock to Peshawar
# Edge costs and heuristic values are illustrative,
# not official road distances.

graph = {
    "Attock": {"Khairabad": 15, "Burhan": 25},
    "Khairabad": {"Attock": 15, "Jahangira": 25},
    "Burhan": {"Attock": 25, "Swabi": 45},
    "Jahangira": {"Khairabad": 25, "Nowshera": 20},
    "Swabi": {"Burhan": 45, "Mardan": 30},
    "Nowshera": {"Jahangira": 20, "Pabbi": 15},
    "Mardan": {"Swabi": 30, "Pabbi": 25},
    "Pabbi": {"Nowshera": 15, "Mardan": 25,
             "Peshawar": 20},
    "Peshawar": {}
}

# Estimated remaining distance to Peshawar (heuristic).
h = {
    "Attock": 90,
    "Khairabad": 75,
    "Burhan": 80,
    "Jahangira": 50,
    "Swabi": 65,
    "Nowshera": 30,
    "Mardan": 40,
    "Pabbi": 15,
    "Peshawar": 0
}

def hill_climbing(start, goal):
    current = start
    path = [current]
    total_cost = 0
    step = 1

    while current != goal:
        print(f"\nStep {step}: Expanding {current}")

        # Display neighboring locations.
        for neighbor, cost in graph[current].items():
            print(
                f"  {neighbor}: road cost={cost} km, "
                f"h={h[neighbor]} km"
            )

        # Select the neighbor with the smallest heuristic.
        neighbors = graph[current]
        if not neighbors:
            print("No neighbors; search failed.")
            return path, total_cost

        best = min(neighbors, key=lambda node: h[node])

        # Hill climbing moves only to a better heuristic.
        if h[best] >= h[current]:
            print("No improvement; local optimum reached.")
            return path, total_cost

        # Update the route and cumulative cost.
        total_cost += neighbors[best]
        current = best
        path.append(current)

        print("Selected:", current)
        print("Cumulative cost:", total_cost, "km")
        step += 1

    return path, total_cost

Start=input("Enter destination :")
Destination=input("Enter destination :")
path, cost = hill_climbing(Start, Destination)

print("\nFinal path:", " -> ".join(path))
print("Total modeled cost:", cost, "km")