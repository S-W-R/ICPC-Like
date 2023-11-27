split_char = ' '

j = input()
s = input()

js = set(j)
res = 0
for i in s:
    if i in js:
        res += 1

print(res)
