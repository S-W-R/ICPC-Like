from heapq import *

split_char = ' '
(number_count,) = [int(x) for x in input().split(split_char)]
values = [100 * int(x) for x in input().split(split_char)]
heapify(values)
res = 0
for i in range(number_count - 1):
    a = heappop(values)
    b = heappop(values)
    ab = a + b
    heappush(values, ab)
    res += (ab * 5) // 100
print(f'{res // 100}.{res % 100}')
