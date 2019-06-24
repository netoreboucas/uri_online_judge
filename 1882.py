# -*- coding: utf-8 -*-


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijsktra(graph, src, dest):
    if src == dest:
        return 0

    visited = {src: 0}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited and (min_node is None or visited[node] < visited[min_node]):
                min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight

    return visited[dest] if dest in visited else None


t = int(input())
for _ in range(t):
    n, m, k = [int(x) for x in raw_input().split()]

    graph = Graph()
    for i in range(n):
        graph.add_node(i)

    for _ in range(m):
        a, b, c = [int(x) for x in raw_input().split()]
        if a != b:
            graph.add_edge(a, b, c)

    cost_boat = dijsktra(graph, 0, n - 1)
    cost_plane = n * k

    if cost_boat is None or cost_plane < cost_boat:
        print '{:0.3f}'.format(cost_plane)
    else:
        print '{:0.3f}'.format(cost_boat)
