split_char = '  '
(count, time) = [int(x) for x in input().split(split_char)]
count -= 1
values = [int(x) for x in input().split(split_char)]
special_id = int(input()) - 1

up_time = values[special_id] - values[0]
down_time = values[-1] - values[special_id]
res = 0
max_distance = values[-1] - values[0]
if down_time <= time or up_time <= time:
    res = max_distance
else:
    res = min(up_time, down_time) + max_distance

print(res)