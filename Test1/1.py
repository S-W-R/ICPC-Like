first = input().split(' ')
second = input().split(' ')
f0 = first[0]
f1 = first[1]
s0 = second[0]
s1 = second[1]
if f0 == s0:
    print(f'{f1} {f0} {s0} {s1}')
elif f0 == s1:
    print(f'{f1} {f0} {s1} {s0}')
elif f1 == s0:
    print(f'{f0} {f1} {s0} {s1}')
elif f1 == s1:
    print(f'{f0} {f1} {s1} {s0}')
else:
    print(-1)
