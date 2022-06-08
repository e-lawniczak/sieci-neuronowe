import random


def ged(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def calculate_dl(a, n):
    r = 2
    while a ** r % n == 1:
        r += 1

    return r


def discrete_log(N):
    a = random.randint(1, N - 1)

    # 1
    value = ged(N, a)

    # 2
    if value > 1:
        return a, 0, value

    # 3
    r = calculate_dl(a, N)

    # 4
    while r % 2 != 0:
        a = random.randint(1, N - 1)
        r = calculate_dl(a, N)

    # 5
    value_plus = ged(N, a ** (r / 2) + 1)
    value_minus = ged(N, a ** (r / 2) - 1)

    # 6.1
    if value_plus > 1:
        return a, r, value_plus
    if value_minus > 1:
        return a, r, value_minus

    # 6.2
    while value_plus == 1 and value_minus == 1:
        a = random.randint(1, N - 1)
        r = calculate_dl(a, N)
        while r % 2 != 0:
            a = random.randint(1, N - 1)
            r = calculate_dl(a, N)

        value_plus = ged(N, a ** (r / 2) + 1)
        value_minus = ged(N, a ** (r / 2) - 1)

        if value_plus > 1:
            return a, r, value_plus
        if value_minus > 1:

            return a, r, value_minus


if __name__ == '__main__':
    print("Laboratoria 8 \n")
    N = 5000
    A, R, Value = discrete_log(N)

    print("Znalzeiono poprawne rozwiązanie dla \nN: {}\na: {} \nr: {} \nNajwiekszy wspolny dzielnik: {}".format(N, A, R, Value))
