import math


def approx_sin(x=1, n=5):
    x, n = float(x), int(n)     # casting x, n from strings into numbers
    sin_x = 0
    for n in range(n):
        term = ((-1)**n * x**(2 * n + 1))/math.factorial(2*n + 1)
        sin_x += term
    return print(f"approx_sin(x={x}, n={n}) =", sin_x)


def approx_cos(x=1, n=5):
    x, n = float(x), int(n)     # casting x, n from strings into numbers
    cos_x = 0
    for n in range(n):
        term = ((-1)**n * x**(2*n))/math.factorial(2*n)
        cos_x += term
    return print(f"approx_cos(x={x}, n={n}) =", cos_x)


def approx_sinh(x=1, n=5):
    x, n = float(x), int(n)     # casting x, n from strings into numbers
    sinh_x = 0
    for n in range(n):
        term = (x**(2 * n + 1))/math.factorial(2*n + 1)
        sinh_x += term
    return print(f"approx_sinh(x={x}, n={n}) =", sinh_x)


def approx_cosh(x=1, n=5):
    x, n = float(x), int(n)     # casting x, n from strings into numbers
    cosh_x = 0
    for n in range(n):
        term = (x**(2*n))/math.factorial(2*n)
        cosh_x += term
    return print(f"approx_cosh(x={x}, n={n}) =", cosh_x)


if __name__ == '__main__':
    # User input
    x = input("Enter x = ")
    n = input("Enter n = ")
    approx_sin(x=x, n=n)
    approx_cos(x=x, n=n)
    approx_sinh(x=x, n=n)
    approx_cosh(x=x, n=n)
