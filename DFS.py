graph = { 
    0: [1, 2], 
    1: [2], 
    2: [0, 3], 
    3: [3] 
} 
visited = set() 
def dfs(graph, node, goal, visited): 
    if node not in visited:  
        visited.add(node) 
        print(node, end=' ') 
        if node == goal: 
            print("\nGoal found!") 
            return True  
        for neighbour in graph[node]: 
            if dfs(graph, neighbour, goal, visited): 
                return True 
    return False 
start_node = 0 
goal_node = 3 
print("Following is Goal-Based Depth First Search:") 
dfs(graph, start_node, goal_node, visited) 