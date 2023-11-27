values = [int(x) for x in input().split(' ')]
a = values[0]
b = values[1]
c = values[2]
t = values[3]
days = t // (a * b * c)
days_remainder = t - days * a * b * c
hours = days_remainder // (b * c)
hours_remainder = days_remainder - hours * b * c
minutes = hours_remainder // c
seconds = hours_remainder - minutes * c
print(f'{hours} {minutes} {seconds}')
