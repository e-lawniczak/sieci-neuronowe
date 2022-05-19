import math
import random

beta = 1.5


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


def calculate_w(s, w, u, x, y, z):
    w_new = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    vec1 = []

    for p in range(4):
        vec1.append(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2])

    for i in range(2):
        for j in range(3):
            for p in range(4):
                w_new[i][j] += (y[p] - z[p]) * d_f(vec1[p]) * s[i] * d_f(
                    w[i][0] * u[p][0] + w[i][1] * u[p][1] + w[i][2] * u[p][2]
                ) * u[p][j]

    return w_new


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

    # print("Maximum: " + str(maximum))
    if maximum < eps:
        return True
    return False


def loop_a(c, eps, losowe=False):
    y = []
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

    s_new = [0.0, 0.0, 0.0]
    w_new = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    x1_vector = []
    x2_vector = []
    t = 0
    l = True
    while True:

        x = calculate_x(w_old, u).copy()
        y = calculate_y(s_old, x).copy()
        if l:
            print(y)
            print(s_old)
            print(w_old)
            l = False
        s_vector = calculate_s(s_old, x, y, z).copy()
        w_vector = calculate_w(s_old, w_old, u, x, y, z).copy()

        for i in range(3):
            s_new[i] = s_old[i] - c * s_vector[i]
        for i in range(2):
            for j in range(3):
                w_new[i][j] = w_old[i][j] - c * w_vector[i][j]

        if calculate_max(w_old, w_new, s_old, s_new, eps):
            y = calculate_y(s_old, x)
            break

        s_old = s_new.copy()
        w_old = w_new.copy()
        t += 1

    if losowe:
        msg = "Wartosci losowe,"
    else:
        msg = "Wartosci stale"
    print(msg + ", \nliczba iteracji: " + str(t))
    print("Wagi w: " + str(w_old))
    print("Wagi s: " + str(s_old))
    print("0 XOR 0 \t" + str(round(y[0], 10)))
    print("1 XOR 0 \t" + str(round(y[1], 10)))
    print("0 XOR 1 \t" + str(round(y[2], 10)))
    print("1 XOR 1 \t" + str(round(y[3], 10)))
    print("Dla wartosci c: {} beta: {} epsilon: {} \n~~~~~~~~~~".format(c, beta, eps))


if __name__ == '__main__':
    print("Laboratoria 5 \n")

    c1 = 0.1
    eps1 = 0.00001
    loop_a(c1, eps1, False)
    loop_a(c1, eps1, True)
