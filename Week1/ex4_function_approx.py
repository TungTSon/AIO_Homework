import math


def approx_sin(x, n=5):
    sin_x = 0
    for n in range(n):
        term = ((-1) ** n * x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_x += term
    return sin_x


def approx_sin(x, n=5):
    sin_x = 0
    for n in range(n):
        term = ((-1)**n * x**(2 * n + 1))/math.factorial(2*n + 1)
        sin_x += term
    return print(sin_x)


def approx_cos(x, n=5):
    cos_x = 0
    for n in range(n):
        term = ((-1)**n * x**(2*n))/math.factorial(2*n)
        cos_x += term
    return print(cos_x)


def approx_sinh(x, n=5):
    sin_x = 0
    for n in range(n):
        term = (x**(2 * n + 1))/math.factorial(2*n + 1)
        sin_x += term
    return print(sin_x)


def approx_cosh(x, n=5):
    cos_x = 0
    for n in range(n):
        term = (x**(2*n))/math.factorial(2*n)
        cos_x += term
    return print(cos_x)


if __name__ == '__main__':
    approx_sin(x=3.14, n=10)
    approx_cos(x=3.14, n=10)
    approx_sinh(x=3.14, n=10)
    approx_cosh(x=3.14, n=10)