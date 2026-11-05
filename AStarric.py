"""
A* Search - Road Route Finder: Attock to Murree
------------------------------------------------
Problem : Find the shortest road route from Attock to Murree
          using a road map of 9 places.

STATE            : the place (city/town) where we currently are.
START STATE      : Attock
GOAL STATE       : Murree
TRANSITION       : drive from one place to a directly connected neighbouring place.
TRANSITION COST  : road distance in km between the two places (approximate values).
HEURISTIC h(n)   : straight-line (air) distance in km from place n to Murree.
                   It never overestimates the real road distance, so it is
                   admissible, and A* is guaranteed to find the optimal path.
                   
A* uses:  f(n) = g(n) + h(n)
    g(n) = actual cost from start to n
    h(n) = estimated cost from n to goal
"""

import heapq
# 1. Road map: place -> {neighbour: distance in km}

road_map = {
    "Attock":      {"Hasan Abdal": 40, "Fateh Jang": 45},
    "Hasan Abdal": {"Attock": 40, "Taxila": 20, "Fateh Jang": 50},
    "Fateh Jang":  {"Attock": 45, "Hasan Abdal": 50, "Rawalpindi": 60},
    "Taxila":      {"Hasan Abdal": 20, "Rawalpindi": 30, "Tarnol": 15},
    "Tarnol":      {"Taxila": 15, "Islamabad": 10},
    "Rawalpindi":  {"Fateh Jang": 60, "Taxila": 30, "Islamabad": 15,
                    "Bhara Kahu": 25, "Murree": 62},
    "Islamabad":   {"Tarnol": 10, "Rawalpindi": 15, "Bhara Kahu": 15, "Murree": 65},
    "Bhara Kahu":  {"Islamabad": 15, "Rawalpindi": 25, "Murree": 42},
    "Murree":      {"Rawalpindi": 62, "Islamabad": 65, "Bhara Kahu": 42},
}
# 2. Heuristic: straight-line distance (km) to the goal (Murree)
heuristic = {
    "Attock": 95,
    "Hasan Abdal": 65,
    "Fateh Jang": 78,
    "Taxila": 56,
    "Tarnol": 42,
    "Rawalpindi": 47,
    "Islamabad": 40,
    "Bhara Kahu": 30,
    "Murree": 0,
}

# 3. A* algorithm
def a_star(start, goal):
    # Open list (priority queue) holds tuples: (f, g, place, path)
    # heapq always gives us the entry with the smallest f first.
    
    open_list = [(heuristic[start], 0, start, [start])]

    # best_g remembers the cheapest cost found so far to reach each place
    best_g = {start: 0}

    # closed set = places already expanded
    closed = set()
    step = 0
    print("-" * 50)
    print("A* NODE EXPANSION STEPS")
    print("-" * 50)
    while open_list:
        # Pick the node with the lowest f = g + h
        f, g, place, path = heapq.heappop(open_list)

        # Skip if this place was already expanded with a cheaper cost
        if place in closed:
            continue
        step += 1
        h = heuristic[place]
        print(f"\nStep {step}: Expand '{place}'   g = {g}, h = {h}, f = {f}")
        print(f"   Path so far: {' -> '.join(path)}")

        # Goal test
        if place == goal:
            print(" Goal reached! ")
            return path, g
        closed.add(place)
        # Generate the successors (neighbouring places)
        for neighbour, distance in road_map[place].items():
            if neighbour in closed:
                continue
            new_g = g + distance            # cost to reach neighbour via this place
            new_f = new_g + heuristic[neighbour]

            # Add only if this is a new place or we found a cheaper way to it
            if neighbour not in best_g or new_g < best_g[neighbour]:
                best_g[neighbour] = new_g
                heapq.heappush(open_list, (new_f, new_g, neighbour, path + [neighbour]))
                print(f"   Add '{neighbour}': g = {new_g}, h = {heuristic[neighbour]}, f = {new_f}")
            else:
                print(f"   Skip '{neighbour}': already have a cheaper route (g = {best_g[neighbour]})")

        # Show the open list after this expansion
        waiting = sorted((item[0], item[2]) for item in open_list if item[2] not in closed)
        print("   Open list (f, place):", waiting)

    return None, None   # no path exists
# 4. Run the program
if __name__ == "__main__":
    start_place = "Attock"
    goal_place = "Murree"
    print(f"Places in the map ({len(road_map)}): {', '.join(road_map)}")
    print(f"Finding the shortest route from {start_place} to {goal_place}")
    path, cost = a_star(start_place, goal_place)
    print("\n" + "-" * 50)
    print("FINAL RESULT")
    print("-" * 50)
    if path:
        print("Optimal path :", " -> ".join(path))
        print("Total cost   :", cost, "km")
    else:
        print("No route found.")