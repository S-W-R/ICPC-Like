import random

arr = [1,1,0,0,1].__iter__()
#monetka = lambda: random.randint(0, 1)
monetka = lambda: arr.__next__()

# monetka = lambda: 0

initial = [2, 3, 4, 5, 6, 1]
current = [e for e in initial]
weights = [
        [None, 10, 5, 7, 2, 10],
        [None, None, 4, 8, 10, 7],
        [None, None, None, 7, 5, 2],
        [None, None, None, None, 9, 10],
        [None, None, None, None, None, 10]
    ]
k_0 = [1, 2, 3, 4, 5, 6]
k_1 = [2, 4, 8, 16, 32, 64]

k = [k_0, k_1]

def distance(a, b):
    if a < b:
        return weights[a - 1][b - 1]
    return weights[b - 1][a - 1]

def find_current_width():
    w = 0
    w += distance(current[-1], current[0])
    for i in range(5):
        w += distance(current[i], current[i + 1])
    return w

current_width = find_current_width()
print(f"{current}, {current_width}")

for i in range(1, 6):
    print(f"Prev {current} {current_width}")
    m = monetka()
    first_place = k[0][i + m - 1]
    second_place = k[1][i + m - 1]
    index_1 = first_place % 6 if first_place % 6 != 0 else 6
    index_2 = second_place % 6 if second_place % 6 != 0 else 6
    print(f"Swap elems {index_1} {index_2}")
    index_1 -= 1
    index_2 -= 1
    current[index_1], current[index_2] = current[index_2], current[index_1]
    new_width = find_current_width()
    print(f"Current {current} {new_width}")
    if new_width >= current_width:
        current[index_1], current[index_2] = current[index_2], current[index_1]
    else:
        current_width = new_width