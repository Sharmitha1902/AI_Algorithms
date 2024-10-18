import heapq

def branch_and_bound_greedy_exit(network, start, goal, cost_fn, heuristic_fn, max_steps):
    
    pq = [(heuristic_fn(start, goal), 0, [start])]
    best_cost = float('inf')
    best_path = None
    steps = 0

    while pq:
        steps += 1
        if steps > max_steps:
            
            return best_path

        
        est_total, curr_cost, path = heapq.heappop(pq)
        curr_node = path[-1]

        if curr_node == goal:
            
            if curr_cost < best_cost:
                best_cost = curr_cost
                best_path = path
            return best_path  

        
        for neighbor in network.get(curr_node, []):
            if neighbor not in path:  
                new_path = path + [neighbor]
                new_cost = curr_cost + cost_fn(curr_node, neighbor)
                
                if new_cost < best_cost:  
                    priority = new_cost + heuristic_fn(neighbor, goal)
                    heapq.heappush(pq, (priority, new_cost, new_path))

    return best_path  


network = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['F'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}


def cost_fn(node1, node2):
    return 1


def heuristic_fn(node, goal):
    return abs(ord(goal) - ord(node))

start = 'S'
goal = 'G'
max_steps = 10

result = branch_and_bound_greedy_exit(network, start, goal, cost_fn, heuristic_fn, max_steps)
print("path found using Branch and Bound Greedy, dead horse:", result)
