from typing import Iterable, Tuple
from collections import deque


class Node:
    def __init__(self, number: int):
        self._edges = set()
        self.number = number
        self.data = None

    def add_edge(self, node: int):
        self._edges.add(node)

    def remove_edge(self, node: int):
        self._edges.remove(node)

    def is_neighbour(self, node: int) -> int:
        return node in self._edges

    def get_neighbours(self) -> Iterable[int]:
        return self._edges


class Graph:
    def __init__(self, count):
        self._nodes = {i: Node(i) for i in range(1, count + 1)}

    def add_edge(self, a: int, b: int):
        self._nodes[a].add_edge(b)
        self._nodes[b].add_edge(a)

    def get_node(self, number: int) -> Node:
        return self._nodes[number]

    @property
    def nodes(self):
        return self._nodes


def max_distance(node: int, graph: Graph) -> Tuple[Node, int]:
    frontier = deque()
    frontier.append(node)
    came_from = {node: None}
    last_node = node
    while frontier:
        current = frontier.popleft()
        last_node = current
        for new_node in graph.get_node(current).get_neighbours():
            if came_from[current] == new_node:
                continue
            elif new_node not in came_from:
                frontier.append(new_node)
                came_from[new_node] = current
    distance = 0
    current = last_node
    while came_from[current] is not None:
        current = came_from[current]
        distance += 1
    return graph.get_node(last_node), distance


def diameter(graph: Graph):
    n1, d1 = max_distance(1, graph)
    n2, d2 = max_distance(n1.number, graph)
    return d2


split_char = ' '
count = int(input())
g1 = Graph(count)
for i in range(count - 1):
    a, b = [float(x) for x in input().split(split_char)]
    g1.add_edge(a, b)
count = int(input())
g2 = Graph(count)
for i in range(count - 1):
    a, b = [float(x) for x in input().split(split_char)]
    g2.add_edge(a, b)
g1_d = diameter(g1)
g1_r = (g1_d // 2) + (g1_d % 2)
g2_d = diameter(g2)
print('L' if g1_r > g2_d else 'D')
