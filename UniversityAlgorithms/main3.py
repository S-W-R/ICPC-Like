from __future__ import annotations
import collections
from typing import NoReturn, TypeVar, Generic, List, Tuple, Iterable, Optional, \
    Dict, Set

INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'out.txt'


def write_correct_answer(filename: str, path: List[int], sum: int) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('Y\n')
        file.write(' '.join(map(str, path)) + '\n')
        file.write(str(sum) + '\n')


def write_incorrect_answer(filename: str) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('N\n')


class Node:
    def __init__(self, number: int, edges: Iterable[Tuple[int, int]]):
        self._edges = dict(edges)
        self.number = number

    def is_neighbour(self, node: int) -> int:
        return node in self._edges

    def get_weight(self, destination: int) -> int:
        return self._edges[destination] if destination in self._edges else None

    def get_neighbours(self) -> Iterable[int]:
        return self._edges.keys()

    def __repr__(self):
        return 'node: ' + str(self.number)


class Graph:
    def __init__(self, graph: List[Node]):
        self._nodes = graph

    def get_node(self, number: int) -> Node:
        return self._nodes[number - 1]

    @property
    def nodes(self) -> Iterable[Node]:
        return self._nodes


class DijkstraData:
    def __init__(self, prev: Optional[int], price: int):
        self.prev = prev
        self.price = price

    def __repr__(self):
        return f'data<prev:{self.prev}, price:{self.price}>'


def parse_task(filename: str) -> Tuple[Graph, int, int]:
    with open(filename, encoding="utf8", mode='r') as file:
        count = int(file.readline())
        raw_graph = []
        for x in range(count):
            raw_node = file.readline()[:-2].rstrip().split(' ')
            neighbours = []
            for i in range(len(raw_node) // 2):
                neighbour = int(raw_node[2 * i])
                cost = int(raw_node[2 * i + 1])
                neighbours.append((neighbour, cost))
            raw_graph.append(Node(x + 1, neighbours))

        init_node = int(file.readline())
        fin_node = int(file.readline())
        return Graph(raw_graph), init_node, fin_node


def dijkstra(graph: Graph, initial: int, final: int) -> Optional[
    Tuple[List[int], int]]:
    notVisited: Set[int] = set(map(lambda x: x.number, graph.nodes))
    track: Dict[int, DijkstraData] = {initial: DijkstraData(None, 0)}
    while True:
        to_open = None
        best_price = float('inf')
        for i in notVisited:
            if i in track and track[i].price < best_price:
                best_price = track[i].price
                to_open = i

        if to_open is None:
            return None
        if to_open == final:
            break
        node = graph.get_node(to_open)
        for i in node.get_neighbours():
            current_price = track[to_open].price + node.get_weight(i)
            if i not in track or track[i].price > current_price:
                track[i] = DijkstraData(to_open, current_price)
        notVisited.remove(to_open)
    result: List[int] = []
    last = final
    while last is not None:
        result.append(last)
        last = track[last].prev
    result.reverse()
    return result, track[final].price


if __name__ == "__main__":
    graph, init, final = parse_task(INPUT_FILE)
    path = dijkstra(graph, init, final)
    if path is not None:
        write_correct_answer(OUTPUT_FILE, path[0], path[1])
    else:
        write_incorrect_answer(OUTPUT_FILE)
