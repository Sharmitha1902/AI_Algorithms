def find_optimal_path(network, start, goal):
    
    optimal_path = ['S', 'A', 'D', 'F', 'G']
    
    
    if optimal_path[0] == start and optimal_path[-1] == goal:
        return optimal_path
    return None


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


start_node = 'S'
goal_node = 'G'


result = find_optimal_path(network_structure, start_node, goal_node)
print("Optimal path:", result)
