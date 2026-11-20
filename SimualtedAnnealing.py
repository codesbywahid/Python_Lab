# Simulated Annealing: Attock to Bahawalpur

import math
import random

graph = {
    "Attock": {"Khairabad": 15, "Burhan": 25},
    "Khairabad": {"Attock": 15, "Jahangira": 25},
    "Burhan": {"Attock": 25, "Swabi": 45},
    "Jahangira": {"Khairabad": 25, "Nowshera": 20},
    "Swabi": {"Burhan": 45, "Mardan": 30},
    "Nowshera": {"Jahangira": 20, "Pabbi": 15},
    "Mardan": {"Swabi": 30, "Pabbi": 25},
    "Pabbi": {"Nowshera": 15, "Mardan": 25, "Peshawar": 20},
    "Peshawar": {"Pabbi": 20, "Kohat": 60},
    "Kohat": {"Peshawar": 60, "Bannu": 70},
    "Bannu": {"Kohat": 70, "Dera Ismail Khan": 90},
    "Dera Ismail Khan": {"Bannu": 90, "Bhakar": 80},
    "Bhakar": {"Dera Ismail Khan": 80, "Sargodha": 100},
    "Sargodha": {"Bhakar": 100, "Faisalabad": 90},
    "Faisalabad": {"Sargodha": 90, "Jhang": 70},
    "Jhang": {"Faisalabad": 70, "Bahawalpur": 120},
    "Bahawalpur": {}
}

h = {
    "Attock": 550,
    "Khairabad": 540,
    "Burhan": 520,
    "Jahangira": 510,
    "Swabi": 500,
    "Nowshera": 480,
    "Mardan": 470,
    "Pabbi": 460,
    "Peshawar": 450,
    "Kohat": 380,
    "Bannu": 300,
    "Dera Ismail Khan": 220,
    "Bhakar": 160,
    "Sargodha": 110,
    "Faisalabad": 80,
    "Jhang": 40,
    "Bahawalpur": 0
}


def simulated_annealing(start, goal,
                        T_start=100.0,
                        T_end=0.1,
                        cooling_rate=0.85,
                        max_iter=100):

    current = start
    path = [current]
    total_cost = 0
    T = T_start
    best_node = current
    best_h = h[current]

    print(f"Start: {current} (h={h[current]})")
    print(f"Initial Temperature: {T}")
    print("-" * 60)

    for iteration in range(1, max_iter + 1):
        if current == goal:
            print(f"\nGoal '{goal}' mil gaya!")
            return path, total_cost

        neighbors = list(graph[current].keys())

        if not neighbors:
            print("No neighbors; search failed.")
            return path, total_cost

        next_node = random.choice(neighbors)

        if next_node in path and next_node != goal:
            continue

        delta = h[next_node] - h[current]   

        if delta < 0:
            accept = True
            reason = "better (accept)"
        else:
            prob = math.exp(-delta / T) if T > 0 else 0
            accept = random.random() < prob
            reason = f"worse, P={prob:.4f} → {'accept' if accept else 'reject'}"

        print(f"Iter {iteration:>2}: {current} -> {next_node} | "
              f"ΔE={delta:>4} | T={T:6.2f} | {reason}")

        if accept:
            total_cost += graph[current][next_node]
            current = next_node
            path.append(current)

            if h[current] < best_h:
                best_node = current
                best_h = h[current]

        T = max(T * cooling_rate, T_end)

    print("\nMax iterations reached.")
    return path, total_cost

Start = input("Enter start location: ")
Destination = input("Enter destination: ")

path, cost = simulated_annealing(Start, Destination)

print("\nFinal path:", " -> ".join(path))
print("Total modeled cost:", cost, "km")