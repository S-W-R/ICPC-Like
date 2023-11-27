from collections import Counter

n, k = map(int, input().split(' '))
ans = 0
count = Counter()
for i in range(n):

    ans += i // k if i % k == 0 else 0
print(ans)

a = '''
3
1 1 2

5
10 20 100 100 100

1000
1 1 1 2 2 2 3 7

1000
1 1 1 1 1 1 1 1 1 1 4 4

1000
1 1 1 1 1 1 1 1 1 1 4 4 4 4 4

1000
1 1 1 2 2 2 3 7 7 7 7 7 7 7 100


1000
7 7 7 7 7 7

1000
1 2 3 4 5 6 7 8 9 9

1000
3 4 5 6 7 8 9 9 9 1000
'''