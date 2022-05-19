def funkcja_progowa(x):
    if x < 0:
        return 0
    return 1


def funkcja_neuronu(wektor_w, wektor_u, i):
    y = 0
    for x in range(i - 1):  # iloczyn skalarny od 1 do m
        y = y + wektor_w[x] * float(wektor_u[x])
    y = y + ((-wektor_w[i-1]) * 1.0)  # ostatnie mnożenie theta * un
    print("Wartość modelu neuronu dla zadanego wejścia: " + str(funkcja_progowa(y)))



def switch(x):
    x = int(x)
    u = list()
    if x == 1:
        # bramka not
        n = 2
        for x in range(n-1):
            u.append(int(input("Podaj u" + str(x + 1))))
        funkcja_neuronu([-2.0, -1.0], u, n-1)
    if x == 2:
        # bramka and
        n = 3
        for x in range(n-1):
            u.append(int(input("Podaj u" + str(x + 1))))
        funkcja_neuronu([6.0, 6.0, 10.0], u, n)
    if x == 3:
        # bramka nand
        n = 3
        for x in range(n-1):
            u.append(int(input("Podaj u" + str(x + 1))))
        funkcja_neuronu([-2.0, -2.0, -3.0], u, n)
    if x == 4:
        # bramka or
        n = 3
        for x in range(n-1):
            u.append(int(input("Podaj u" + str(x + 1) +" ")))
        funkcja_neuronu([3.0, 3.0, 2.0], u, n)



if __name__ == '__main__':
    print("Laboratoria 1 \n")
    print("NOT - 1\nAND - 2\nNAND - 3\nOR - 4")
    bramka = input("wybierz bramkę: \n")
    switch(bramka)




