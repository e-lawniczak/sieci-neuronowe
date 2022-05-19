def getClearVector(val):
    tempVec = list()
    for i in range(25):
        tempVec.append(val)
    return tempVec


def createInitialVectors():
    vectorsBase = list()
    tmp = list()

    # u0
    tmp = getClearVector(-1.0)
    tmp[6] = 1.0
    tmp[7] = 1.0
    tmp[8] = 1.0
    tmp[11] = 1.0
    tmp[13] = 1.0
    tmp[16] = 1.0
    tmp[17] = 1.0
    tmp[18] = 1.0
    vectorsBase.append(tmp)

    # u1
    tmp = getClearVector(-1.0)
    tmp[6] = 1.0
    tmp[7] = 1.0
    tmp[12] = 1.0
    tmp[17] = 1.0
    vectorsBase.append(tmp)

    # u0'
    tmp = getClearVector(-1.0)
    tmp[1] = 1.0
    tmp[2] = 1.0
    tmp[3] = 1.0
    tmp[6] = 1.0
    tmp[8] = 1.0
    tmp[11] = 1.0
    tmp[13] = 1.0
    tmp[16] = 1.0
    tmp[17] = 1.0
    tmp[18] = 1.0
    vectorsBase.append(tmp)

    # u1'
    tmp = getClearVector(-1.0)
    tmp[2] = 1.0
    tmp[7] = 1.0
    tmp[12] = 1.0
    tmp[17] = 1.0
    tmp[22] = 1.0
    vectorsBase.append(tmp)
    return vectorsBase


def printVector(vector, n, mode=True):
    for i in range(len(vector)):
        if mode:
            if vector[i] > 0:
                print("#", end="\t")
            else:
                print("-", end="\t")
        else:
            print("{:.2f}".format(vector[i]), end="\t")
        if (i + 1) % n == 0 and i != n*n - 1:
            print()

    print('\n')

def printTable(vector, n, m, mode=True):

    for i in range(n):
        for j in range(m):
            if mode:
                if vector[i][j] > 0:
                    print("#", end="\t")
                else:
                    print("-", end="\t")
            else:
                print("{:.2f}".format(vector[i][j]), end="\t")
        print()

    print('\n')

def sgn(y):
    if y < 0:
        return -1.0
    return 1.0

def calc_sgn(vector):
    out = list()
    for i in vector:
        out.append(sgn(i))

    return out

def w(z0, z1):
    outW = [[0.0 for x in range(25)] for y in range(25)]
    for i in range(25):
        for j in range(25):
            outW[i][j] = 1.0/25.0 * ((z0[i] * z0[j]) + (z1[i] * z1[j]))
    return outW


def f(vectorW, vectorU):
    out = list()
    for i in range(25):
        tmp = 0.0
        for j in range(25):
            tmp = tmp + vectorW[i][j] * vectorU[j]
        out.append(tmp)
    #return out
    return calc_sgn(out)


if __name__ == '__main__':
    print("Laboratoria 3 \n")
    initialVectors = createInitialVectors()
    vectorW = w(initialVectors[0], initialVectors[1])

    printVector(initialVectors[2], 5)


    result = f(vectorW, initialVectors[2])
    printVector(result, 5, mode=True)

    printVector(initialVectors[3], 5)

    result = f(vectorW, initialVectors[3])
    printVector(result, 5, mode=True)



