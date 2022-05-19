import random


def get_25_vec():
    vec = [[0.0 for i in range(25)] for j in range(25)]
    return vec


def get_z_vector(f=1):
    t = [
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
    ]

    t2 = [
        0.0, 1.0, 1.0, 1.0, 0.0,
        0.0, 1.0, 0.0, 1.0, 0.0,
        0.0, 1.0, 0.0, 1.0, 0.0,
        0.0, 1.0, 0.0, 1.0, 0.0,
        0.0, 1.0, 1.0, 1.0, 0.0,
    ]
    if f == 2:
        return t2
    return t


def printVector(vector, n=5, mode=True):
    for i in range(len(vector)):
        if mode:
            if vector[i] > 0:
                print("#", end="  ")
            else:
                print("-", end="  ")
        if (i + 1) % n == 0 and i != n * n - 1:
            print()

    print('\n')


def get_x_vector():
    vec = [int(random.random() * 1000 % 2) for i in range(25)]

    return vec


def calculate_c(z):
    c = get_25_vec()
    for i in range(25):
        for j in range(25):
            if i != j:
                c[i][j] = (z[i] - 0.5) * (z[j] - 0.5)
            else:
                c[i][j] = 0.0
    return c


def calculate_w(c, d=None):
    w = get_25_vec()
    for i in range(25):
        for j in range(25):
            if d == None:
                w[i][j] = 2 * c[i][j]
            else:
                w[i][j] = 2 * (c[i][j] + d[i][j])
    return w


def calculate_next_x(u, x_vec):
    x = x_vec.copy()
    for i in range(25):
        if u[i] < 0:
            x[i] = 0
        elif u[i] > 0:
            x[i] = 1
    return x


def sum_w_x(w, x):
    s = 0
    for j in range(25):
        s += w[j] * x[j]
    return s


def theta(c, d=None):
    s = 0
    for j in range(25):
        if d == None:
            s += c[j]
        else:
            s += c[j] + d[j]

    return s


def hopfield2(t):
    x_vec = get_x_vector()
    z_vec = get_z_vector()
    z2_vec = get_z_vector(2)
    c_vec = calculate_c(z_vec)
    d_vec = calculate_c(z2_vec)
    w_vec = calculate_w(c_vec, d_vec)
    u_vec = [0.0 for i in range(25)]

    printVector(x_vec)

    while t != 0:

        t -= 1

        for i in range(25):
            val = sum_w_x(w_vec[i], x_vec) - theta(c_vec[i], d_vec[i])
            u_vec[i] = val
        # print(u_vec)
        x_vec = calculate_next_x(u_vec, x_vec).copy()

        printVector(x_vec)


def hopfield1(t):
    x_vec = get_x_vector()
    z_vec = get_z_vector()
    c_vec = calculate_c(z_vec)
    w_vec = calculate_w(c_vec)
    u_vec = [0.0 for i in range(25)]

    printVector(x_vec)

    while t != 0:

        t -= 1

        for i in range(25):
            val = sum_w_x(w_vec[i], x_vec) - theta(c_vec[i])
            u_vec[i] = val
        # print(u_vec)
        x_vec = calculate_next_x(u_vec, x_vec).copy()

        printVector(x_vec)


if __name__ == '__main__':
    print("Laboratoria 11 \n")
    ask = input("Wybierz 1 lub 2")
    max_t = 1
    if int(ask) == 1:
        hopfield1(max_t)
    else:
        hopfield2(max_t)
