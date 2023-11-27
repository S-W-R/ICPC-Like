split_char = ' '
count = int(input())
(table_x, table_y) = [int(x) for x in input().split(split_char)]
ans_cost = 1001

for i in range(count):
    (x, y, cost) = [int(x) for x in input().split(split_char)]
    if (x >= table_x and y >= table_y) or (x >= table_y and y >= table_x):
        ans_cost = min(ans_cost, cost)
print(ans_cost)
