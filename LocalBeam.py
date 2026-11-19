# Local Beam Search: Attock to Bahawalpur

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


def local_beam_search(start, goal, k=3):
    beams = [(start, [start], 0)]

    step = 1
    while True:
        print(f"\n========== Step {step} ==========")
        print("Current beams:")
        for i, (node, path, cost) in enumerate(beams):
            print(f"  Beam {i+1}: {node} (h={h[node]}, cost={cost} km)")

        for node, path, cost in beams:
            if node == goal:
                print(f"\nGoal '{goal}' mil gaya!")
                return path, cost

        all_candidates = []
        for node, path, cost in beams:
            for neighbor, edge_cost in graph[node].items():
                if neighbor in path:
                    continue
                new_path = path + [neighbor]
                new_cost = cost + edge_cost
                all_candidates.append((neighbor, new_path, new_cost))

        if not all_candidates:
            print("Koi candidate nahi mila; search failed.")
            return beams[0][1], beams[0][2]

        all_candidates.sort(key=lambda x: h[x[0]])
        beams = all_candidates[:k]

        print(f"\nTop {k} candidates selected:")
        for i, (node, path, cost) in enumerate(beams):
            print(f"  {i+1}. {node} (h={h[node]}, cost={cost} km)")

        step += 1

        if step > 50:
            print("Max steps reached.")
            return beams[0][1], beams[0][2]

Start = input("Enter start location: ")
Destination = input("Enter destination: ")
K = int(input("Enter beam width (k): ") or "3")

best_path, best_cost = local_beam_search(Start, Destination, k=K)

print("\nFinal best path:", " -> ".join(best_path))
print("Total modeled cost:", best_cost, "km")