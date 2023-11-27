split_char = ' '
(n, m) = [int(x) for x in input().split(split_char)]

max_length = max(len(str(n - 1)), len(str(m - 1)))

n_max = n - 1
m_max = m - 1



n = str(n_max)
while len(n) < max_length:
    n = '0' + n
m = str(n_max)
while len(m) < max_length:
    m = '0' + m

i = max_length - 1
j = 0

res = 1

while True:
    if i ==0 or j == max_length:
        break
    ni = int(n[i])
    mi = int(m[j])
    if mi == 0 or ni == 0:
        break

    

    i -= 1
    j += 1


print(res)
