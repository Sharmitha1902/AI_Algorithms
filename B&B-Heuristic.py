import heapq

def branch_and_bound_search(network, start, goal, heuristic_fn):
    
    priority_queue = [(heuristic_fn(start, goal), [start])]
    visited = set()
    
    while priority_queue:
        
        _, path = heapq.heappop(priority_queue)
        current = path[-1]
        
        
        if current == goal:
            return path
        
        
        if current not in visited:
            visited.add(current)
            
            for neighbor in network.get(current, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    
                    priority_value = heuristic_fn(neighbor, goal)
                    heapq.heappush(priority_queue, (priority_value, new_path))
    
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


def simple_heuristic(node, target):
    return ord(target) - ord(node)


start_node = 'S'
target_node = 'G'


found_path = branch_and_bound_search(network_structure, start_node, target_node, simple_heuristic)
print("Path found using Branch and Bound Heuristics:", found_path)
