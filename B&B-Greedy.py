import heapq

def branch_and_bound_greedy(network, start, goal, cost_fn, heuristic_fn):
    
    priority_queue = [(0 + heuristic_fn(start, goal), 0, [start])]
    best_cost = float('inf')
    best_path = None
    
    while priority_queue:
        #
        _, current_cost, path_so_far = heapq.heappop(priority_queue)
        current_node = path_so_far[-1]
        
        
        if current_node == goal:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path_so_far
            continue
        
        
        for neighbor in network.get(current_node, []):
            if neighbor not in path_so_far:  
                new_path = path_so_far + [neighbor]
                total_cost = current_cost + cost_fn(current_node, neighbor)
                
                
                if total_cost < best_cost:
                    estimated_priority = total_cost + heuristic_fn(neighbor, goal)
                    heapq.heappush(priority_queue, (estimated_priority, total_cost, new_path))
    
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


def simple_cost(node1, node2):
    return 1  


def simple_heuristic(node, goal):
    return ord(goal) - ord(node)  


start_node = 'S'
target_node = 'G'


found_path = branch_and_bound_greedy(network_structure, start_node, target_node, simple_cost, simple_heuristic)
print("path found using Branch and Bound Greedy:", found_path)
