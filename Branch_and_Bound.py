import heapq

def branch_and_bound_search(network, start, goal, edge_cost):
    
    frontier = [(0, [start])]
    best_cost = float('inf')
    best_path = None

    while frontier:
        
        current_cost, current_path = heapq.heappop(frontier)
        current_node = current_path[-1]

        
        if current_node == goal:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = current_path
            continue  
        
        for neighbor in network.get(current_node, []):
            if neighbor not in current_path:  
                new_cost = current_cost + edge_cost(current_node, neighbor)
                if new_cost < best_cost:
                    new_path = current_path + [neighbor]
                    heapq.heappush(frontier, (new_cost, new_path))

    return best_path

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


def edge_cost(node1, node2):
    return 1


start_node = 'S'
goal_node = 'G'
optimal_path = branch_and_bound_search(network_structure, start_node, goal_node, edge_cost)

print("path found using branch and bound:", optimal_path)
