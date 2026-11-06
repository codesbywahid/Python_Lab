import heapq
roads = [
    ("Comsats", "Park Road", 2),
    ("Park Road", "G-11", 4),
    ("Park Road", "Saidpur Road", 3),
    ("Park Road", "F-10", 6),
    ("G-11", "Saidpur Village", 3),
    ("Saidpur Village", "Saidpur Road", 6),
    ("Saidpur Road", "Peshawar Mor", 5),
    ("Peshawar Mor", "F-7", 4),
    ("Peshawar Mor", "Faisalabad", 6),
    ("F-7", "Blue Area", 5),
    ("F-10", "Jinnah Avenue", 5),
    ("Jinnah Avenue", "Blue Area", 4),
    ("Blue Area", "Faisal Mosque", 7),
]
h = {
    "Comsats": 15,
    "Park Road": 13,
    "F-10": 12,
    "Jinnah Avenue": 9,
    "Saidpur Road": 10,
    "Peshawar Mor": 8,
    "F-7": 6,
    "Blue Area": 4,
    "Faisalabad": 9,
    "G-11": 12,
    "Saidpur Village": 13,
    "Faisal Mosque": 0,
}
graph = {}
for a, b, km in roads:
    graph.setdefault(a, []).append((b, km))
    graph.setdefault(b, []).append((a, km))
start = input("Enter starting point: ")
goal = input("Enter Destination: ")
to_check = [(h[start], 0, start, [start])]
best_g = {start: 0}
while to_check:
    f, g, place, path = heapq.heappop(to_check)
    if g != best_g.get(place):
        continue
    if place == goal:
        print("Route:", " -> ".join(path))
        print("Total distance:", g, "km")
        break
    for neighbour, km in graph[place]:
        new_g = g + km

        if new_g < best_g.get(neighbour, float("inf")):
            best_g[neighbour] = new_g
            new_f = new_g + h[neighbour]

            heapq.heappush(
                to_check,
                (new_f, new_g, neighbour, path + [neighbour])
            )
else:
    print("No route found.")