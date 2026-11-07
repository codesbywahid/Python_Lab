import heapq
graph={
    "S":["A","B"],
    "A":["C","G"],
    "B":["D","E"],
    "C":[],
    "D":[],
    "E":[]
}
h={
    "S":7,
    "A":4,
    "B":2,
    "C":5,
    "D":3,
    "E":6,
    "G":0
}
def greedy_best_first(start,goal):
    pq =[(h[start],start,[start])]
    visited=[]

    while pq:
        hueristic,node,path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.append(node)
        print("Expanding",node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,(h[neighbor],neighbor,path+[neighbor])
                )
    print("Goal not found")
print("Path: ",greedy_best_first('S','G'))