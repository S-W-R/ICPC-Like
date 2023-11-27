VOWELS = set('a,e,i,o,u,y'.split(','))

nickname = input()
is_correct = True
for l, r in zip(nickname, nickname[1::]):
    if (l in VOWELS and r in VOWELS) or (l not in VOWELS and r not in VOWELS):
        is_correct = False
        break
print('YES' if is_correct else 'NO')
