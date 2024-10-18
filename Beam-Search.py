import heapq

def beam_search(network, start, goal, max_beam_size, heuristic):
    
    paths_beam = [(heuristic(start, goal), [start])]

    while paths_beam:
        expanded_beam = []

        
        for _, path in paths_beam:
            current = path[-1]  

        
            if current == goal:
                return path

            
            for adjacent in network.get(current, []):
                new_path = path + [adjacent]
                expanded_beam.append((heuristic(adjacent, goal), new_path))

        
        paths_beam = heapq.nsmallest(max_beam_size, expanded_beam)

    
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


def heuristic(node, target):
    return abs(ord(target) - ord(node))


start = 'S'
goal = 'G'
max_beam_size = 2


result = beam_search(network, start, goal, max_beam_size, heuristic)
print("Beam Search path:", result)
