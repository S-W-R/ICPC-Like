from __future__ import annotations
from typing import NoReturn, List, Tuple, Dict, Set

INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'out.txt'


class Graph:
    def __init__(self, vertexes: List[Tuple[int, int, int]]):
        self._vertexes = vertexes
        self._edges = {}  # type: Dict[int, Set[int]]
        for i in range(len(self._vertexes)):
            self._edges[i] = set()
            for j in range(len(self._vertexes)):
                if i == j:
                    continue
                a1, b1, c1 = self._vertexes[i]
                a2, b2, c2 = self._vertexes[j]
                if (a1 < a2 and b1 < b2) or (a1 < b2 and b1 < a2):
                    self._edges[i].add(j)
        self._max_heights = {}  # type: Dict[int, int]

    def _max_height(self, i: int) -> int:
        if i in self._max_heights:
            return self._max_heights[i]
        l1, l2, w = self._vertexes[i]
        max_w = w + max(map(self._max_height, self._edges[i]), default=0)
        self._max_heights[i] = max_w
        return max_w

    def result(self) -> int:
        return max(map(self._max_height, range(len(self._vertexes))))


class GraphSetup:
    def __init__(self):
        self._vertexes = []  # type: List[Tuple[int, int, int]]

    def add_vertex(self, a: int, b: int, c: int):
        self._vertexes.append((a, b, c))
        self._vertexes.append((a, c, b))
        self._vertexes.append((b, c, a))

    def create(self) -> Graph:
        return Graph(self._vertexes)


def main() -> NoReturn:
    result = []  # type List[int]
    with open(INPUT_FILE, encoding='utf8', mode='r') as file:
        count = int(file.readline())
        while count != 0:
            graph_setup = GraphSetup()
            for i in range(count):
                (x, y, z) = [int(x) for x in file.readline().split()]
                graph_setup.add_vertex(x, y, z)
            graph = graph_setup.create()
            result.append(graph.result())
            count = int(file.readline())
    with open(OUTPUT_FILE, encoding='utf8', mode='w') as file:
        for i in range(len(result)):
            file.write(f'Case {i + 1}: maximum height = {result[i]}\n')


if __name__ == '__main__':
    main()
