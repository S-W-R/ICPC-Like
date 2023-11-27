split_char = ' '
(n, ) = [int(x) for x in input().split(split_char)]
items = [int(x) for x in input().split(split_char)]


target = items[0] + items[n - 1]
res = target

i = 0
j = n - 1

while (i < j):
    if (items[i] + items[j] == target):
        i += 1
        j -= 1
    else:
        res = -1
        break

print(res)