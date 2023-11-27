split_char = ' '
(count,) = [int(x) for x in input().split(split_char)]
graph = dict()
reversed_graph = dict()
answ = True
for i in range(1, count + 1):
    (n,) = [int(x) for x in input().split(split_char)]
    if n in graph:
        if graph[n] == i or (i in reversed_graph and reversed_graph[i] == n):
            answ = False
            break
        graph[i] = graph[n]
        reversed_graph[n] = reversed_graph[i]
    else:
        graph[i] = n
        reversed_graph[n] = i


if answ:
    print('She can do everything')
else:
    print('Poor Polina')
