split_char = ' '
(n, m) = [int(x) for x in input().split(split_char)]

max_length = max(len(str(n - 1)), len(str(m - 1)))


def convert(h, maxl):
    r = 0
    for i in range(maxl):
        r = (r * 10) + h % 10
        h = h // 10
    return r


res = 0
for i in range(n):
    min = convert(i, max_length)
    if min < m:
        res += 1
print(res)
