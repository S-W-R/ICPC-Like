split_char = ' '
(n, ) = [int(x) for x in input().split(split_char)]
items = [int(x) for x in input().split(split_char)]

res = -1
sum_i = sum(items)
if sum_i % n != 0 or n % 2 != 0:
    res = -1
else:
    pair_sum = 2 * (sum_i // n)
    res = pair_sum
    for i in range(len(items)):
        left = items[i]
        right = items[-(i + 1)]
        if left + right != pair_sum:
            res = -1
            break
print(res)