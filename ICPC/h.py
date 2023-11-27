split_char = ' '
(count,) = [int(x) for x in input().split(split_char)]

order = []
items = set()
modifier = 1
for i in range(1, count + 1):
    (k, b) = [int(x) for x in input().split(split_char)]
    if k == 1:
        order.append(i)
    else:
        items.add((k, b, i))
        modifier *= k
count = len(items)
for i in range(count):
    selected = max(items, key=lambda x: (modifier // x[0]) * x[1])
    order.append(selected[2])
    items.remove(selected)
    modifier = modifier // selected[0]

print(' '.join(map(lambda x: str(x), order)))
