import random

def BMS(network, start, goal):
    path = [start]  
    
    
    while path[-1] != goal:
        current = path[-1]
        if current in network and network[current]:  
            next_node = random.choice(network[current])  
            path.append(next_node)  
        else:
            break  

    return path


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


found_path = BMS(network, start, goal)
print("Path found using BMS:", found_path)


