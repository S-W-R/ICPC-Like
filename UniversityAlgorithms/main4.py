from __future__ import annotations
import collections
from typing import NoReturn, TypeVar, Generic, List, Tuple, Iterable, \
    Optional, Dict, Set

INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'out.txt'


class Edge:
    def __init__(self, v1: int, v2: int, d: int):
        self.v1 = v1
        self.v2 = v2
        self.d = d

    def __repr__(self):
        return f'[{self.v1}-{self.v2}:{self.d}]'


def distance(v1: Tuple[int, int, int], v2: Tuple[int, int, int]) -> int:
    x1, y1, i1 = v1
    x2, y2, i2 = v2
    d = abs(x1 - x2) + abs(y1 - y2)
    return d


def parse_graph(filename: str) -> Tuple[int, List[Edge]]:
    raw_v = []
    with open(filename, encoding="utf8", mode='r') as file:
        count = int(file.readline())
        for i in range(count):
            x, y = [int(j) for j in
                    file.readline().split(' ')]
            raw_v.append((x, y, i))
    raw_e = list(
        filter(lambda g: g[0] != g[1], [(x, y) for x in raw_v for y in raw_v]))
    edges = map(lambda x: Edge(x[0][2], x[1][2], distance(x[0], x[1])), raw_e)
    return count, list(edges)


def kruskal(count: int, edges: List[Edge]) -> List[Edge]:
    c2v = {i: set([i, ]) for i in range(count)}  # type: Dict[int, Set[int]]
    v2c = {i: i for i in range(count)}  # type: Dict[int, int]
    sorted_edges = sorted(edges, key=lambda x: x.d)
    edges = []
    for e in sorted_edges:
        c1 = v2c[e.v1]
        c2 = v2c[e.v2]
        if c1 != c2:
            c1s = c2v[c1]
            c2s = c2v[c2]
            c2v[c1] = c1s.union(c2s)
            for another in c2s:
                v2c[another] = c1
            edges.append(e)
    return edges


def write_answer(filename, result: int, spisok: List[List[int]]) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        for i in range(len(spisok)):
            file.write(
                ' '.join(map(lambda x: str(x + 1), spisok[i])) + ' 0 \n')
        file.write(str(result))


def main() -> NoReturn:
    c, e = parse_graph(INPUT_FILE)
    out_edges = kruskal(c, e)
    spisok = {i: set() for i in range(c)}  # type: Dict[int, Set[int]]
    res = 0
    for e in out_edges:
        res += e.d
        spisok[e.v1].add(e.v2)
        spisok[e.v2].add(e.v1)
    spisok2 = list(range(c))  # type: List[List[int]]
    for i in range(c):
        spisok2[i] = list(sorted(spisok[i]))
    write_answer(OUTPUT_FILE, res, spisok2)


if __name__ == '__main__':
    main()
