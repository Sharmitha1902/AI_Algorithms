from collections import deque

def bfs(network, start, goal):
    queue = deque([(start, [start])])
    explored = set()
    
    while queue:
        current_node, path_traversed = queue.popleft()
        if current_node not in explored:
            if current_node == goal:
                return path_traversed
            explored.add(current_node)
            for neighbor in network.get(current_node, []):
                queue.append((neighbor, path_traversed + [neighbor]))
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

start = 'S'
goal = 'G'


found_path = bfs(network, start, goal)
print("BFS path:", found_path)
