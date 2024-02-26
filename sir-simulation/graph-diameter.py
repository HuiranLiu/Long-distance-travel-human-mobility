import random
import sys
from collections import deque


input_graph = sys.argv[1]
num_4sweep = int(sys.argv[2])

def read_graph(file_path):
    input_graph = {}
    with open(file_path, 'r') as file:
        for line in file.readlines():
            # split the line at the colon
            parts = line.split(':', 1)

            # if the line isn't in the correct format, skip it
            if len(parts) != 2:
                continue

            # extract the node and the adjacent nodes
            node, adj_list_str = parts

            # convert the node to an integer, while replacing the infectious marker if necessary
            if "_I" in node:
                node = node.replace("_I", "")
            node = int(node.strip())

            # split the adjacent nodes string by commas and convert to integers
            adj_nodes = [int(adj_node.strip()) for adj_node in adj_list_str.split(',') if adj_node.strip().isdigit()]

            input_graph[node] = adj_nodes

    return input_graph


def bfs(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    farthest_node = start
    max_distance = 0

    while queue:
        vertex, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
            farthest_node = vertex

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return farthest_node, max_distance


def four_sweep_approximation(graph):
    # first Sweep
    random_vertex = random.choice(list(graph.keys()))
    u, _ = bfs(graph, random_vertex)

    # second Sweep
    v, _ = bfs(graph, u)

    # third Sweep
    w, _ = bfs(graph, v)

    # fourth Sweep
    x, max_distance = bfs(graph, w)

    return max_distance

print("Reading input graph: " + input_graph)
graph = read_graph(input_graph)

print("Approximating diameter by taking the maximum of " + str(num_4sweep)+ " 4-Sweep runs ...")
approx_diameters = list()
for i in range(0, num_4sweep):
    approx_diameter = four_sweep_approximation(graph)
    approx_diameters.append(approx_diameter)
    
approx_diameter_max = max(approx_diameters)

print("Result: " + str(approx_diameter_max))


