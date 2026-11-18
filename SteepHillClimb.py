# Steepest Ascent Hill Climbing: Attock to Bahawalpur

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


def steepest_ascent_hill_climbing(start, goal):
    current = start
    path = [current]
    total_cost = 0
    step = 1

    while current != goal:
        print(f"\nStep {step}: Expanding {current}")

        neighbors = graph[current]
        if not neighbors:
            print("No neighbors; search failed.")
            return path, total_cost

        for neighbor, cost in neighbors.items():
            print(f"  {neighbor}: road cost={cost} km, h={h[neighbor]} km")

        best = min(neighbors, key=lambda node: h[node])
        print(f"  --> Best neighbor selected: {best} (h={h[best]})")

        if h[best] >= h[current]:
            print("No improvement; local optimum reached.")
            return path, total_cost

        total_cost += neighbors[best]
        current = best
        path.append(current)

        print("Selected:", current)
        print("Cumulative cost:", total_cost, "km")
        step += 1

    return path, total_cost

Start = input("Enter start location: ")
Destination = input("Enter destination: ")

path, cost = steepest_ascent_hill_climbing(Start, Destination)

print("\nFinal path:", " -> ".join(path))
print("Total modeled cost:", cost, "km")