from heapq import *


class Eater:
    def __init__(self, current_time: int, eat_time: int):
        self.current_time = current_time
        self.last_eat_time = current_time
        self.eat_time = eat_time
        self.sleep_time = eat_time

    @property
    def priority(self):
        return self.current_time + self.eat_time

    def eat(self):
        self.last_eat_time = self.current_time + self.eat_time
        self.current_time = self.last_eat_time + self.sleep_time

    def __lt__(self, other):
        return self.priority < other.priority


if __name__ == '__main__':
    values = [int(x) for x in input().split(' ')]
    n = values[0]
    m = values[1]
    heap = []
    for eater in [Eater(0, int(x)) for x in input().split(' ')]:
        heappush(heap, eater)
    for i in range(n):
        eater = heappop(heap)
        eater.eat()
        heappush(heap, eater)
    max_time = -1
    for item in sorted(heap):
        max_time = max(max_time, item.last_eat_time)
    print(max_time)
