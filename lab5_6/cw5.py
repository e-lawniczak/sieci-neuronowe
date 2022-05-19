import math
import random

beta = 2.8


def f(x) -> float:
    return 1.0 / (1.0 + math.exp(-beta * x))


def d_f(x) -> float:
    return (beta * math.exp(-beta * x)) / pow((math.exp(-beta * x) + 1.0), 2)


def calculate_x1(w, u):
    x1 = []
    for p in range(4):
        val = f(w[0][0] * u[p][0] + w[0][1] * u[p][1] + w[0][2] * u[p][2])
        x1.append(val)
    return x1


def calculate_x2(w, u):
    x2 = []
    for p in range(4):
        val = f(w[1][0] * u[p][0] + w[1][1] * u[p][1] + w[1][2] * u[p][2])
        x2.append(val)
    return x2


def calculate_x(w, u):
    x_vector = [
        [],
        [],
        [],
        []
    ]
    for p in range(4):
        x_vector[p].append(f(w[0][0] * u[p][0] + w[0][1] * u[p][1] + w[0][2] * u[p][2]))
        x_vector[p].append(f(w[1][0] * u[p][0] + w[1][1] * u[p][1] + w[1][2] * u[p][2]))
        x_vector[p].append(1.0)

    return x_vector


def calculate_y(s, x):
    y = [0.0, 0.0, 0.0, 0.0]
    for p in range(4):
        y[p] = f(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2])
    return y


def calculate_s(s, x, y, z):
    s_new = [0.0, 0.0, 0.0]

    for i in range(3):
        for p in range(4):
            s_new[i] += (y[p] - z[p]) * d_f(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2]) * x[p][i]

    return s_new


def calculate_single_s(s, x, y, z, k):
    total = 0
    for p in range(4):
        total += (y[p] - z[p]) * d_f(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2]) * x[p][k]

    return total


def calculate_w(s, w, u, x, y, z):
    w_new = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    vec1 = []
    vec2 = [0.0, 0.0, 0.0]

    for p in range(4):
        vec1.append(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2])

    for i in range(2):
        for p in range(4):
            vec2.append(w[i][0] * u[p][0] + w[i][1] * u[p][1] + w[i][2] * u[p][2])

    for i in range(2):
        for j in range(3):
            for p in range(4):
                w_new[i][j] += (y[p] - z[p]) * d_f(vec1[p]) * s[i] * d_f(vec2[p]) * u[p][j]

    return w_new


def calculate_single_w(s, w, u, x, y, z, i, j):
    total = 0

    for p in range(4):
        s_sum = s[0]*x[p][0] + s[1]*x[p][1] + s[2]*x[p][2]
        w_sum = w[i][0]*u[p][0] + w[i][1]*u[p][1] + w[i][2]*u[p][2]
        total += (y[p] - z[p]) * d_f(s_sum) * s[i] * d_f(w_sum) * u[p][j]

    return total


def calculate_max(w_old, w_new, s_old, s_new, eps):
    max_w = 0.0
    max_s = 0.0

    for i in range(2):
        for j in range(3):
            if abs(w_new[i][j] - w_old[i][j]) > max_w:
                max_w = abs(w_new[i][j] - w_old[i][j])

    for j in range(3):
        if abs(s_new[j] - s_old[j]) > max_s:
            max_s = abs(s_new[j] - s_old[j])

    maximum = max(max_w, max_s)

    print("Maximum: " + str(maximum) + str(maximum > eps))
    if maximum > eps:
        return True
    return False


def loop_a(c, eps, losowe=False):
    y = [0.0, 0.0, 0.0, 0.0]
    x = []
    z = [0.0, 1.0, 1.0, 0.0]
    u = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    if losowe:
        w_old = [[round(random.uniform(-5, 5), 1) for i in range(3)] for j in range(2)]
        s_old = [round(random.uniform(-5, 5), 1) for i in range(3)]
    else:
        w_old = [
            [0.0, 1.0, 2.0],
            [0.0, 1.0, 2.0],
        ]
        s_old = [0.0, 1.0, 2.0]

    s_new = s_old.copy()
    w_new = w_old.copy()

    x = calculate_x(w_old, u).copy()
    y = calculate_y(s_old, x).copy()

    s_new[0] = s_old[0] - c * calculate_single_s(s_old, x, y, z, 0)
    s_new[1] = s_old[1] - c * calculate_single_s(s_old, x, y, z, 1)
    s_new[2] = s_old[2] - c * calculate_single_s(s_old, x, y, z, 2)

    w_new[0][0] = w_old[0][0] - c * calculate_single_w(s_old, w_old, u, x, y, z, 0, 0)
    w_new[0][1] = w_old[0][1] - c * calculate_single_w(s_old, w_old, u, x, y, z, 0, 1)
    w_new[0][2] = w_old[0][2] - c * calculate_single_w(s_old, w_old, u, x, y, z, 0, 2)
    w_new[1][0] = w_old[1][0] - c * calculate_single_w(s_old, w_old, u, x, y, z, 1, 0)
    w_new[1][1] = w_old[1][1] - c * calculate_single_w(s_old, w_old, u, x, y, z, 1, 1)
    w_new[1][2] = w_old[1][2] - c * calculate_single_w(s_old, w_old, u, x, y, z, 1, 2)

    t = 0

    while calculate_max(w_old, w_new, s_old, s_new, eps):
        t += 1
        s_old[0] = s_new[0]
        s_old[1] = s_new[1]
        s_old[2] = s_new[2]

        w_old[0][0] = w_new[0][0]
        w_old[0][1] = w_new[0][1]
        w_old[0][2] = w_new[0][2]
        w_old[1][0] = w_new[1][0]
        w_old[1][1] = w_new[1][1]
        w_old[1][2] = w_new[1][2]

        s_new[0] = s_old[0] - c * calculate_single_s(s_old, x, y, z, 0)
        s_new[1] = s_old[1] - c * calculate_single_s(s_old, x, y, z, 1)
        s_new[2] = s_old[2] - c * calculate_single_s(s_old, x, y, z, 2)

        w_new[0][0] = w_old[0][0] - c * calculate_single_w(s_old, w_old, u, x, y, z, 0, 0)
        w_new[0][1] = w_old[0][1] - c * calculate_single_w(s_old, w_old, u, x, y, z, 0, 1)
        w_new[0][2] = w_old[0][2] - c * calculate_single_w(s_old, w_old, u, x, y, z, 0, 2)
        w_new[1][0] = w_old[1][0] - c * calculate_single_w(s_old, w_old, u, x, y, z, 1, 0)
        w_new[1][1] = w_old[1][1] - c * calculate_single_w(s_old, w_old, u, x, y, z, 1, 1)
        w_new[1][2] = w_old[1][2] - c * calculate_single_w(s_old, w_old, u, x, y, z, 1, 2)




    print("Koniec uczenia, \nliczba iteracji: " + str(t))
    print("Wagi w: " + str(w_old))
    print("Wagi s: " + str(w_new))
    print("0 XOR 0 \t" + str(round(y[0], 10)))
    print("1 XOR 0 \t" + str(round(y[1], 10)))
    print("0 XOR 1 \t" + str(round(y[2], 10)))
    print("1 XOR 1 \t" + str(round(y[3], 10)))


if __name__ == '__main__':
    print("Laboratoria 5 \n")

    c1 = 0.1
    eps1 = 0.0001
    loop_a(c1, eps1, False)
