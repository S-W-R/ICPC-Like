split_char = ' '
(min_value, max_value) = [int(x) for x in input().split(split_char)]


# values = [int(x) for x in input().split(split_char)]
def iteration():
    numbers = [str(x) for x in range(1, 10)]
    i = 1
    yield 0
    while True:
        for j in numbers:
            x = j * i
            yield int(x)
        i += 1


res = 0
for x in iteration():
    if x > max_value:
        break
    if x >= min_value:
        res += 1
print(res)
