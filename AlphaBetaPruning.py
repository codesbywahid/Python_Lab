INF = float('inf')

route_names = ["Route A (Highway)", "Route B (City Road)", "Route C (Ring Road)"]

tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, 1]],
    [[7, 4], [8, 3]],
]

def alphabeta(node, is_max, alpha, beta):
    # Base case: Agar leaf node (number) hai toh return karo
    if isinstance(node, int):
        return node

    if is_max:
        best = -INF
        for child in node:
            value = alphabeta(child, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            
            # Pruning Condition
            if alpha >= beta:
                print(f"  Pruned at MAX node (alpha={alpha}, beta={beta})")
                break
        return best
    else:
        best = INF
        for child in node:
            value = alphabeta(child, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            
            # Pruning Condition
            if alpha >= beta:
                print(f"  Pruned at MIN node (alpha={alpha}, beta={beta})")
                break
        return best

alpha = -INF
beta = INF
best_route = ""
best_value = -INF

print("--- Evaluating Routes ---")

for i in range(len(tree)):
    value = alphabeta(tree[i], True, alpha, beta) 
    
    print(f"{route_names[i]} -> value = {value}")
    
    # Update best route and alpha
    if value > best_value:
        best_value = value
        best_route = route_names[i]
        alpha = max(alpha, best_value)

print("\n--- Final Result ---")
print("Best value at root:", best_value)
print("Best route:", best_route)