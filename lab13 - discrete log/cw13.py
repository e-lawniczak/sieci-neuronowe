import random


def ged(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def calculate_dl(a, n):
    r = 1
    MAX = 100

    while a ** r % n == 1:
        r += 1
        if r > MAX:
            return -1

    return r


def discrete_log(N):
    MAX = 1000

    while True:
        MAX -= 1
        if MAX == 0:
            return 0,0,0
        # 1
        a = random.randint(1, N - 1)

        # 2
        value = ged(N, a)
        if value > 1:
            return a, 0, value

        # 3
        r = calculate_dl(a, N)

        # 4
        if r % 2 == 0:
            # 5
            value_plus = ged(N, a ** (r / 2) + 1)
            value_minus = ged(N, a ** (r / 2) - 1)
            if value_plus > 1:
                return a, r, value_plus
            if value_minus > 1:
                return a, r, value_minus



if __name__ == '__main__':
    print("Laboratoria 8 \n")
    N = [random.randint(100, 100000) for i in range(5)]
    N = [12, 91, 57, 143, 1737, 1859, 13843, 988027] + N
    for n in N:
        A, R, Value = discrete_log(n)
        if A == 0:
            print("Nie znaleziono dzielnika")
        else:
            print("N: {} a: {} r: {} \n\tdzielnik: {}\n".format(n, A, R, Value))
        input()
