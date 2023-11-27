from heapq import *
split_char = '  '
(number_count, operation_count) = [int(x) for x in input().split(split_char)]
values = [int(x) for x in input().split(split_char)]


def get_numbers(n):
    numbers = []
    a = 1
    while n > 0:
        b = (9 - n % 10) * a
        n = n // 10
        if b > 0:
            numbers.append(b)
        a *= 10
    return numbers

heap = []
current_count = 0
for i in values:
    for j in get_numbers(i):
        if current_count < operation_count:
            heappush(heap, j)
            current_count += 1
        else:
            heappushpop(heap, j)
res = 0
for i in heap:
    res += i
print(res)

