from __future__ import annotations
import collections
from typing import NoReturn, TypeVar, Generic, List, Tuple, Iterable, Optional


INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'out.txt'


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @staticmethod
    def zero() -> Point:
        return Point(0, 0)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, obj):
        return isinstance(obj, Point) and obj.x == self.x and obj.y == self.y

    def __ne__(self, obj):
        return not self == obj

    def __hash__(self):
        return 397 * self.x.__hash__() ** self.y.__hash__()

    def __str__(self):
        return f"x: {self.x}; y: {self.y};"


T = TypeVar('T')


class Matrix(Generic[T]):
    value: T

    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            raise ValueError()
        self._width = width
        self._height = height
        self._matrix = self.__init_matrix(self._width, self._height)

    @staticmethod
    def __init_matrix(width: int, height: int) -> List[List[T]]:
        matrix = list()
        for i in range(width):
            column = list()
            matrix.append(column)
            for j in range(height):
                column.append(None)
        return matrix

    @staticmethod
    def from_point(point: Point) -> Matrix:
        return Matrix(point.x, point.y)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def in_borders(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def __contains__(self, item: Point) -> bool:
        return self.in_borders(item.x, item.y)

    def __getitem__(self, key: Point) -> T:
        if not self.in_borders(key.x, key.y):
            raise IndexError()
        return self._matrix[key.x][key.y]

    def __setitem__(self, key: Point, value: T) -> NoReturn:
        if not self.in_borders(key.x, key.y):
            raise IndexError()
        self._matrix[key.x][key.y] = value


NEAR_POINTS = [Point(-1, 0), Point(1, 0), Point(0, 1), Point(0, -1)]


def parse_task(filename: str) -> Tuple[Point, Point, Matrix]:
    with open(filename, encoding="utf8", mode='r') as file:
        height = int(file.readline())
        width = int(file.readline())
        table = Matrix(width, height)
        for y in range(height):
            values = [bool(int(j)) for j in
                      file.readline().split(maxsplit=width)]
            for x in range(width):
                table[Point(x, y)] = values[x]
        init_pos = tuple(int(j) - 1 for j in file.readline().split(maxsplit=2))
        init_cord = Point(init_pos[1], init_pos[0])
        fin_pos = tuple(int(j) - 1 for j in file.readline().split(maxsplit=2))
        final_cord = Point(fin_pos[1], fin_pos[0])
    return init_cord, final_cord, table


def get_neighbours(position: Point, matrix: Matrix) -> Iterable[Point]:
    for near_pos in NEAR_POINTS:
        new_point = position + near_pos
        if new_point in matrix and matrix[new_point] == 0:
            yield new_point


def bfs(matrix: Matrix, start: Point, finish: Point) -> Optional[List[Point]]:
    frontier = collections.deque()
    frontier.append(start)
    came_from = {start: None}
    is_found = False
    while frontier:
        if is_found:
            break
        current = frontier.popleft()
        for new_node in get_neighbours(current, matrix):
            if new_node not in came_from:
                frontier.append(new_node)
                came_from[new_node] = current
                if new_node == finish:
                    is_found = True
                    break
    if finish not in came_from:
        return None
    current = finish
    chain = [current]
    while came_from[current] is not None:
        current = came_from[current]
        chain.append(current)
    return chain[::-1]


def write_correct_answer(filename: str, path: List[Point]) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('A\n')
        for point in path:
            file.write(f'{point.y + 1} {point.x + 1}\n')


def write_incorrect_answer(filename: str) -> NoReturn:
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('N\n')


if __name__ == "__main__":
    init, finish, matrix = parse_task(INPUT_FILE)
    path = bfs(matrix, init, finish)
    if path is not None:
        write_correct_answer(OUTPUT_FILE, path)
    else:
        write_incorrect_answer(OUTPUT_FILE)
