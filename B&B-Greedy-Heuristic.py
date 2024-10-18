import heapq

def branch_bound_heuristic(network, start, goal, cost_fn, heuristic_fn):
    
    queue = [(heuristic_fn(start, goal), 0, [start])]
    visited = set()

    while queue:
        
        estimated_cost, path_cost, path = heapq.heappop(queue)
        current_node = path[-1]

        
        if current_node == goal:
            return path

        
        if current_node not in visited:
            visited.add(current_node)

            for neighbor in network.get(current_node, []):
                if neighbor not in visited:
                    
                    new_path = path + [neighbor]
                    new_cost = path_cost + cost_fn(current_node, neighbor)
                    priority = new_cost + heuristic_fn(neighbor, goal)

                    
                    heapq.heappush(queue, (priority, new_cost, new_path))

    return None  


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


def uniform_cost(node1, node2):
    return 1


def simple_heuristic(node, goal):
    return abs(ord(goal) - ord(node))

start_node = 'S'
goal_node = 'G'


result = branch_bound_heuristic(network, start_node, goal_node, uniform_cost, simple_heuristic)
print("path found using Branch and Bound Greedy heuristics:", result)

