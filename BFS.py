import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
graph = {
    "Adam": ["Basia", "Emil", "Creslaw"],
    "Basia": ["Adam", "Daria", "Franek"],
    "Creslaw": ["Adam", "Franek"],
    "Daria": ["Basia", "Emil"],
    "Emil": ["Daria", "Adam"],
    "Franek": ["Basia", "Creslaw"]
}
def BFS(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            print("Shortest Route:", " -> ".join(path))
            print("Connections:", len(path) - 1)
            return path

        for friend in graph[current]:
            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])

    print("No route found.")
    return []

start = input("Starting name: ")
goal = input("Destination name: ")

if start not in graph or goal not in graph:
    print("User not found.")
else:
    path = BFS(graph, start, goal)

    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=10)

    nx.draw(G, pos, with_labels=True,
            node_color="lightblue",
            node_size=2500,
            font_weight="bold")

    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            G, pos, edgelist=edges,
            edge_color="red", width=4
        )
        nx.draw_networkx_nodes(
            G, pos, nodelist=path,
            node_color="white", node_size=2500
        )

    plt.title("Friendship Graph - Shortest Route in Red")
    plt.show()