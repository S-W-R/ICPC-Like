number = input()
answer = {1}
if number[-1] != '*':
    first = int(number[-1])
    if first % 2 == 0:
        answer.add(2)
    if first == 5:
        answer.add(5)
    if first == 0:
        answer.add(5)
        answer.add(10)
    if number[-2] != '*':
        second = int(number[-2])
        if second * 10 + first % 4 == 0:
            answer.add(4)
        if number[-3] != '*':
            third = int(number[-3])
            if third * 100 + second * 10 + first % 8 == 0:
                answer.add(8)

print(' '.join(map(lambda x: str(x), sorted(answer))))
