def hill_climb_search(network, start, goal, heuristic):
    """
    Performs hill climbing search from the start node to the goal node using a heuristic function.
    """
    current = start
    path = [current]

    while current != goal:
        neighbors = network.get(current, [])
        
        if not neighbors:
            print(f"No more neighbors to explore from node '{current}'")
            return None  

        
        next_node = min(neighbors, key=lambda n: heuristic(n, goal))
        
        
        if heuristic(next_node, goal) >= heuristic(current, goal):
            print(f"Stuck at node '{current}' — no better neighbors.")
            return None

        current = next_node
        path.append(current)

    return path


network_structure = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['F'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}


def heuristic_func(node, goal):
    return abs(ord(goal) - ord(node))


start = 'S'
goal = 'G'
result = hill_climb_search(network_structure, start, goal, heuristic_func)

if result:
    print("Hill Climbing path:", result)
else:
    print("No valid path found.")
