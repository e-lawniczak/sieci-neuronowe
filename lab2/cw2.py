def getClearVector(val):
    tempVec = list()
    for i in range(26):
        tempVec.append(val)
    return tempVec


def createInitialVectors():
    vectorsBase = list()
    tmp = list()

    # u1
    tmp = getClearVector(0.0)
    tmp[6] = 1.0
    tmp[7] = 1.0
    tmp[8] = 1.0
    tmp[11] = 1.0
    tmp[13] = 1.0
    tmp[16] = 1.0
    tmp[17] = 1.0
    tmp[18] = 1.0
    tmp[25] = 1.0
    vectorsBase.append(tmp)

    # u2
    tmp = getClearVector(0.0)
    tmp[10] = 1.0
    tmp[11] = 1.0
    tmp[12] = 1.0
    tmp[15] = 1.0
    tmp[17] = 1.0
    tmp[20] = 1.0
    tmp[21] = 1.0
    tmp[22] = 1.0
    tmp[25] = 1.0
    vectorsBase.append(tmp)

    # u3
    tmp = getClearVector(0.0)
    tmp[6] = 1.0
    tmp[7] = 1.0
    tmp[12] = 1.0
    tmp[17] = 1.0
    tmp[22] = 1.0
    tmp[25] = 1.0
    vectorsBase.append(tmp)

    # 4
    tmp = getClearVector(0.0)
    tmp[2] = 1.0
    tmp[3] = 1.0
    tmp[8] = 1.0
    tmp[13] = 1.0
    tmp[25] = 1.0
    vectorsBase.append(tmp)

    # u5
    tmp = getClearVector(0.0)
    tmp[5] = 1.0
    tmp[6] = 1.0
    tmp[11] = 1.0
    tmp[16] = 1.0
    tmp[21] = 1.0
    tmp[25] = 1.0
    vectorsBase.append(tmp)
    return vectorsBase


def printallVectors(vectors):
    for y in vectors:
        for i in range(len(y)):
            print(str(y[i]), end='\t')
            if (i + 1) % 5 == 0 and i != 24:
                print()

        print('\n')


def scalar(vector_w, vector_u):
    output = 0.0
    for x in range(26):
        output += vector_w[x] * vector_u[x]
    if output >= 0:
        return 1.0
    return 0.0


def main_func(c):
    uVectors = createInitialVectors()
    wVector = getClearVector(1.0)
    time = 1
    counter = 0.0
    # c = float(input("Podaj wartosc c"))

    while counter < 5.0:
        if (time-1) % 5 >= 2:
            zt = 1.0
        else:
            zt = 0.0
        scalarSum = scalar(wVector, uVectors[(time-1) % 5])
        for i in range(26):
            wVector[i] = wVector[i] + c * (zt - scalarSum) * uVectors[(time-1) % 5][i]
        time += 1

        if scalarSum == zt:
            counter += 1.0
        else:
            counter = 0

    print("time = " + str(time))
    # for i in range(26):
    #     print(wVector[i], end="\n")

    for i in range(len(wVector)):
        print("{:.2f}".format(wVector[i]), end="\t")
        if (i + 1) % 5 == 0 and i != 24:
            print()

    print('\n')

if __name__ == '__main__':


    main_func(1.0)
    main_func(0.1)
    main_func(0.01)

