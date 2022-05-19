def vprint(vector):
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            if vector[i][j] > 0:
                print("#", end="  ")
            else:
                print("-", end="  ")
        print()


def get_u_vectors():
    v_list = list()

    # u1 
    tmp = [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 1.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0],
    ]
    v_list.append(tmp)

    # u2 
    tmp = [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 1.0, 1.0, 0.0, 0.0],
        [1.0, 0.0, 1.0, 0.0, 0.0],
        [1.0, 1.0, 1.0, 0.0, 0.0],
    ]
    v_list.append(tmp)

    # u3 
    tmp = [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0],
    ]
    v_list.append(tmp)

    # u4 
    tmp = [
        [0.0, 0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0],
    ]
    v_list.append(tmp)

    # u5 
    tmp = [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0],
    ]
    v_list.append(tmp)

    return v_list


def get_w_vectors():
    v_list = list()

    # w1
    tmp = [
        [1.0, 1.0, 1.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ]
    v_list.append(tmp)

    # w2
    tmp = [
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
    ]
    v_list.append(tmp)

    # w3
    tmp = [
        [1.0, 1.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0],
    ]
    v_list.append(tmp)

    # w4
    tmp = [
        [0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0],
    ]
    v_list.append(tmp)

    return v_list


def get_clear_vector(val):
    vec = list()
    for i in range(5):
        vec.append([0.0, 0.0, 0.0, 0.0, 0.0])

    return vec


def threshold_function(value):
    if value >= 0:
        return 1
    return 0


def threshold_function2(value):
    return value


def calculate_x_i_j(i, j, w, u):
    val = 0
    for a in range(3):
        for b in range(3):
            try:
                val += w[a][b] * u[i - (a)][j - (b)]
            except IndexError:
                print("ERROR:")
                print("a: {} b: {} i: {} j: {}".format(a, b, i, j))
                break
    return val


def convolution(w, u):
    x_vector = get_clear_vector(0.0)

    for i in range(len(x_vector)):
        for j in range(len(x_vector[i])):
            x_vector[i][j] = threshold_function(calculate_x_i_j(i, j, w, u))

    return x_vector


def calculate_y(x, i, j):
    val = 0
    for k in range(4):
        for l in range(4):
            val += x[i + k][j + l]

    return val


def pooling(x_vector, w, u):
    # x_vector = get_clear_vector(0.0)
    #
    # for i in range(len(x_vector)):
    #     for j in range(len(x_vector[i])):
    #         x_vector[i][j] = threshold_function2(calculate_x_i_j(i, j, w, u))

    y = [
        [0.0, 0.0],
        [0.0, 0.0],
    ]

    for i in range(2):
        for j in range(2):
            y[i][j] = threshold_function((1/4**2) * calculate_y(x_vector, i, j))

    return y


if __name__ == '__main__':
    print("Laboratoria 8 \n")
    w_vec = get_w_vectors()
    u_vec = get_u_vectors()
    i_count = 1
    j_count = 1
    for item_u in u_vec:

        j_count = 1
        for item_w in w_vec:
            x_vec = convolution(item_w, item_u)
            print("For i = {} j = {} convolution x is: \n".format(i_count, j_count))
            vprint(x_vec)

            j_count += 1
        i_count += 1