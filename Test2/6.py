split_char = ' '
(count,) = [int(x) for x in input().split(split_char)]
values = [int(x) for x in input().split(split_char)]

is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0

even = -1
odd = -1
i = 1
for v in values:
    if is_even(i) and not is_even(v):
        if even >= 0:
            even = -1
            odd = -1
            break
        else:
            even = i
    if not is_even(i) and is_even(v):
        if odd >= 0:
            even = -1
            odd = -1
            break
        else:
            odd = i
    i += 1
if not (even >= 0 and odd >= 0):
    even = -1
    odd = -1
print(f'{even} {odd}')
