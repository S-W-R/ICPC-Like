import collections
from typing import List, Tuple, Set, Optional, NoReturn, Dict

INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'out.txt'
NEAR_POINTS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def cordFromGraph(index: int, size: Tuple[int, int]) -> Tuple[int, int]:
    width, height = size
    return (index // width) + 1, index - (index // width) * width + 1


def cordToIndex(cord: Tuple[int, int], size: Tuple[int, int]) -> int:
    x, y = cord
    width, height = size
    return (y - 1) * height + x - 1



def parse_task(filename: str) -> Tuple[int, int, List[List[bool]]]:
    with open(filename, encoding="utf8", mode='r') as file:
        height = int(file.readline())
        width = int(file.readline())
        size = (width, height)
        raw_graph = [[] for i in range(height * width)]
        table: Dict[Tuple[int, int], bool] = {}
        for y in range(1, height + 1):
            values = [bool(int(j)) for j in
                      file.readline().split(maxsplit=width)]
            for x in range(1, width + 1):
                table[(x, y)] = values[x]
        init_pos = tuple(int(j) for j in file.readline().split(maxsplit=2))
        init_i = cordToIndex(init_pos, size)
        final_pos = tuple(int(j) for j in file.readline().split(maxsplit=2))
        final_i = cordToIndex(final_pos, size)
    for x in range(1, width + 1):
        for y in range(1, height + 1):
            cord = (x, y)
            for near in NEAR_POINTS:
                xn, yn = near
                near_cord = (x + xn, y + yn)


    return init_i, final_i, raw_graph


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


def bfs(graph1: List[List[bool]], start: int) -> Set[int]:
    frontier = collections.deque()
    frontier.append(start)
    came_from = {start: None}
    while frontier:
        current = frontier.popleft()
        for new_node in get_neighbours(graph1, current):
            if came_from[current] == new_node:
                continue
            if new_node not in came_from:
                frontier.append(new_node)
                came_from[new_node] = current
            else:
                new_node_neighbours = set(get_neighbours(graph1, new_node))
                tmp = current
                while came_from[tmp] is not None:
                    tmp = came_from[tmp]
                    if tmp in new_node_neighbours:
                        break
    return set(came_from.keys())


if __name__ == "__main__":
    '''
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
        write_correct_answer(OUTPUT_FILE)'''
