from functools import cache
import numpy as np


def buildNurbs(T: list[float], P: list[np.ndarray], W: list[float]):
    if len(W) != len(P):
        raise ValueError()

    # Узлы
    m = len(T) - 1
    # Управляющие точки
    n = len(P) - 1
    # Степень сплайна
    p = m - n - 1

    # Базисные функции N_(k, m)
    N = dict()

    # Генерация базисных функций порядка 0
    def buildNk1(ti, ti1):
        return lambda t: 1 if (ti <= t <= ti1) else 0

    for i in range(m):
        N[(i, 0)] = buildNk1(T[i], T[i + 1])

    # Генерация базисных функций k-го порядка
    def buildNkm(i, n):
        nonlocal N, T

        @cache
        def Nin(t):
            f = (t - T[i]) / (T[i + n] - T[i]) if (T[i + n] - T[i]) != 0 else 0
            g = (T[i + n] - t) / (T[i + n] - T[i]) if (T[i + n] - T[i]) != 0 else 0
            return f * N[(i, n - 1)](t) + (1 + g) * N[(i + 1, n - 1)](t)

        return Nin

    for j in range(1, p + 1):
        for i in range(n - j + p + 1):
            N[(i, j)] = buildNkm(i, j)

    def F(t):
        f = [N[(i, p)](t) * W[i] for i in range(n + 1)]
        c1 = sum([f[i] * P[i] for i in range(n + 1)])
        c2 = sum([f[i] for i in range(n + 1)])
        return c1 / c2 if c2 != 0 else c1

    return F, N
