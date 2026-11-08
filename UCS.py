import heapq
def ucs_heapq_list(graph, start, goal):
    queue = [(0, start, [start])]   # (cost, node, path)
    visited = []   # list to store visited nodes
    while queue:
        cost, node, path = heapq.heappop(queue)  # pop smallest cost
        print(f"Expanding {node}, Cost: {cost}, Path: {path}")
        print("-------------------------------------------")

        # If already visited, skip
        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Goal found!")
            print("Path:", path)
            print("Total Cost:", cost)
            return

        # Expand neighbors
        for neighbor, edge_cost in graph[node]:
            cumulative_cost = cost + edge_cost
            heapq.heappush(queue, (cumulative_cost, neighbor, path + [neighbor]))
        
    print("goal not found")

graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Oradea', 71)],
    'Oradea': [('Sibiu', 151)],
    'Timisoara': [('Lugoj', 111)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Pitesti',97),('Craiova',146)],
    'Lugoj': [('Mehedia', 70)],
    'Mehedia': [('Drobeta', 75)],
    'Drobeta': [('Craiova',120)],
    'Craiova': [('Pitesti',138)],
    'Fagaras': [('Bucharest',211)],
    'Pitesti': [('Bucharest',101)],
    'Bucharest': [('Giurgiu',90),('Urziceni',85)],
    'Giurgiu':[],
    'Urziceni':[('Vaslui',142),('Hirsova',98)],
    'Hirsova':[('Eforie',86)],
    'Vaslui':[('Iasi',92)],
    'Iasi':[('Neamt',87)],
    'Neamt':[],
    'Eforie':[]

}
start=input("Enter starting point : ")
goal=input("Enter destination : ")
ucs_heapq_list(graph,start,goal)