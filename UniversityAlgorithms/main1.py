import collections
from typing import List, Tuple, Set, Optional, NoReturn

INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'out.txt'


def parse_graph(filename: str) -> List[List[bool]]:
    raw_graph = []
    with open(filename, encoding="utf8", mode='r') as file:
        count = int(file.readline())
        for i in range(count):
            values = [bool(int(j)) for j in
                      file.readline().split(maxsplit=count)]
            raw_graph.append(values)
    return raw_graph


def write_correct_answer(filename: str) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('A')


def write_incorrect_answer(filename: str, cycle1: List[int]) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('N\n')
        file.write(cycle1.__str__())


def get_neighbours(graph1: List[List[bool]], node: int) -> List[int]:
    neighbours = []
    for i in range(len(graph1)):
        if graph1[node][i]:
            neighbours.append(i)
    return neighbours


def bfs(graph1: List[List[bool]], start: int) -> Tuple[Set[int], List[int]]:
    frontier = collections.deque()
    frontier.append(start)
    came_from = {start: None}
    cycle: Optional[List[int]] = None
    while frontier:
        current = frontier.popleft()
        for new_node in get_neighbours(graph1, current):
            if came_from[current] == new_node:
                continue
            if new_node not in came_from:
                frontier.append(new_node)
                came_from[new_node] = current
            else:
                cycle = [new_node, current]
                new_node_neighbours = set(get_neighbours(graph1, new_node))
                tmp = current
                while came_from[tmp] is not None:
                    tmp = came_from[tmp]
                    cycle.append(tmp)
                    if tmp in new_node_neighbours:
                        break
    return set(came_from.keys()), cycle


if __name__ == "__main__":
    graph1 = parse_graph(INPUT_FILE)
    visited = set()
    is_cycle_found = False
    for i in range(len(graph1)):
        if i in visited:
            continue
        new_visited, cycle1 = bfs(graph1, i)
        visited.update(new_visited)
        if cycle1 is not None:
            write_incorrect_answer(OUTPUT_FILE, sorted(cycle1))
            is_cycle_found = True
            break

    if not is_cycle_found:
        write_correct_answer(OUTPUT_FILE)
