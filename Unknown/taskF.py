from collections import Counter

n = int(input())
p = sorted(filter(lambda j: j > 0, [int(i) for i in input().split(' ', n)]))
weights = sorted(set(p))
counter = Counter(p)
birds = [(i, counter[i]) for i in weights]
answer = 0
last_all_count = 0
last_all_value = 0
new_count = 0
for i in range(len(birds)):
    bird = birds[i]
    bird_value = bird[0]
    bird_count = bird[1]
    new_count += bird_count
    value_dif = bird_value - last_all_value
    if value_dif <= new_count:
        answer += value_dif
        last_all_value = bird_value
        last_all_count = last_all_count + new_count
        new_count = 0
    if i == len(birds) - 1:
        answer += new_count
print(answer)
