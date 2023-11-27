from heapq import *

split_char = ' '
(length, count) = [int(x) for x in input().split(split_char)]


class Pointer:
    def __init__(self, time: int, is_start: bool, x1, y1, x2, y2):
        self.time = time
        self.is_start = is_start
        self.gradient = lambda n: (y2 - y1) / (x2 - x1) * (n - x1) + y1
        self.y1 = y1
        self.y2 = y2

    @property
    def priority(self):
        return -self.time

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f'point: {self.time}|{self.is_start}'


array = list(map(lambda x: list(), range(length + 1)))
for i in range(count):
    (x1, y1, x2, y2) = [int(x) for x in input().split(split_char)]
    x1 -= 1
    x2 -= 1
    array[x1].append(Pointer(i, True, x1, y1, x2, y2))
    array[x2 + 1].append(Pointer(i, False, x1, y1, x2, y2))

heap = []
current = None  # Pointer
closed = set()
for i in range(length):
    for pointer in array[i]:
        if not pointer.is_start:
            closed.add(pointer.time)
        else:
            heappush(heap, pointer)
    if len(heap) > 0:
        current = heap[0]
    if current is None or current.time in closed:
        current = None
    while heap and current is None:
        current = heap[0]
        if current.time in closed:
            current = None
            heappop(heap)
    if current is not None:
        array[i] = current.gradient(i)
    else:
        array[i] = 0.0

print(' '.join(map(lambda x: str(x), array[:-1])))
