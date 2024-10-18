import heapq

def a_star_search(network, start, goal, cost_func, heuristic_func):
    priority_queue = [(0 + heuristic_func(start, goal), 0, [start])]
    explored = set()
    
    while priority_queue:
        _, current_cost, path = heapq.heappop(priority_queue)
        current_node = path[-1]
        
        if current_node == goal:
            return path
        
        if current_node not in explored:
            explored.add(current_node)
            for neighbor in network.get(current_node, []):
                if neighbor not in explored:
                    new_path = path + [neighbor]
                    total_cost = current_cost + cost_func(current_node, neighbor)
                    priority_value = total_cost + heuristic_func(neighbor, goal)
                    heapq.heappush(priority_queue, (priority_value, total_cost, new_path))
    
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

def cost_func(node1, node2):
    return 1  
def heuristic_func(node, goal):
    return abs(ord(goal) - ord(node))  
start = 'S'
goal = 'G'

path_result = a_star_search(network, start, goal, cost_func, heuristic_func)
print("A* algorithm result:", path_result)

