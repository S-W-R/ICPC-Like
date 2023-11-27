split_char = ' '
degree = int(input())
values = [float(x) for x in input().split(split_char)]
if degree == 1:
    a0, a1 = values
    f = lambda x: a0 + a1 * x
    f_prime = lambda x: a1
if degree == 3:
    a0, a1, a2, a3, = values
    f = lambda x: a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3
    f_prime = lambda x: a1 + 2 * a2 * x + 3 * a3 * x ** 2
if degree == 5:
    a0, a1, a2, a3, a4, a5 = values
    f = lambda x: (
            a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 + a4 * x ** 4 + a5 * x ** 5)
    f_prime = lambda x: (
            a1 + 2 * a2 * x + 3 * a3 * x ** 2 + 4 * a4 * x ** 3 + 5 * a5 * x ** 4)


def newton(func, func_prime, x0=0, eps=1e-8, kmax=1e3):
    x, x_prev, i = x0, x0 + 2 * eps, 0
    while abs(x - x_prev) >= eps and i < kmax:
        x, x_prev, i = x - func(x) / func_prime(x), x, i + 1
    return x


res = newton(f, f_prime)
print(res)
