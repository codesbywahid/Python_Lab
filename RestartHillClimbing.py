# Random Restart Hill Climbing: Attock to Peshawar
# Edge costs and heuristic values are illustrative,
# not official road distances.

import random

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

    while current != goal:
        neighbors = graph[current]

        if not neighbors:
            return path, total_cost, False  

        best = min(neighbors, key=lambda node: h[node])

        if h[best] >= h[current]:
            return path, total_cost, False

        total_cost += neighbors[best]
        current = best
        path.append(current)

    return path, total_cost, True  


def random_restart_hill_climbing(start, goal, max_restarts=10):

    possible_starts = [node for node in graph if node != goal]

    best_path, best_cost, success = hill_climbing(start, goal)
    best_start = start

    print(f"\n--- Restart 0: Start = {start} ---")
    print("Path:", " -> ".join(best_path))
    print("Cost:", best_cost, "km | Success:", success)

    if success:
        print("Goal mil gaya pehli hi koshish mein.")
        return best_path, best_cost

    for i in range(1, max_restarts + 1):
        new_start = random.choice(possible_starts)

        print(f"\n--- Restart {i}: Start = {new_start} ---")
        path, cost, success = hill_climbing(new_start, goal)

        print("Path:", " -> ".join(path))
        print("Cost:", cost, "km | Success:", success)

        if success and (not success or cost < best_cost):
            best_path, best_cost, best_start = path, cost, new_start

        if success:
            print(f"Goal mil gaya! Best start: {best_start}")
            return best_path, best_cost

    print("\nMax restarts khatam. Best solution jo mila:")
    return best_path, best_cost


Start = input("Enter start location: ")
Destination = input("Enter destination: ")

best_path, best_cost = random_restart_hill_climbing(Start, Destination, max_restarts=10)

print("\nFinal best path:", " -> ".join(best_path))
print("Total modeled cost:", best_cost, "km")