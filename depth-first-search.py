def dfs(network, start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        node, path = stack.pop()
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path
            
            for neighbor in network.get(node, []):
                stack.append((neighbor, path + [neighbor]))
    
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

start = 'S'
goal = 'G'


result = dfs(network_structure, start, goal)
print("DFS path:", result)
