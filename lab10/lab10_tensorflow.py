import random
import tensorflow as tf
import numpy as np

np.random.seed(50)
N = 5
EPOCHS = 1000


def init():
    X = tf.Variable(np.random.uniform(-N, N), trainable=True)
    Y = tf.Variable(np.random.uniform(-N, N), trainable=True)
    return X, Y


def function(X, Y):
    return 3 * X ** 4 + 4 * X ** 3 - 12 * X ** 2 + 12 * Y ** 2 - 24 * Y


def preform_sgd():
    X, Y = init()
    # for i in range(5):
    optimizer = tf.optimizers.SGD(learning_rate=0.01, momentum=0.99)
    for epoch in range(EPOCHS):
        optimizer.minimize(lambda: function(X, Y), var_list=[X, Y])
        print("X: {}\nY: {}\nFunction value: {}".format(X.numpy(), Y.numpy(), function(X.numpy(), Y.numpy())), end="\r")
        # print(X.numpy(), end="\r")
        # print(Y.numpy(), end="\r")
        # print(function(X.numpy(), Y.numpy()), end="\r")
        # print(str(X.numpy()) + " " +str(Y.numpy()) + " " +str(function(X.numpy(), Y.numpy())), end="\r")

    print("\n\nFinal result")
    print("X: {}\nY: {}\nFunction: {}".format(X.numpy(), Y.numpy(), function(X.numpy(), Y.numpy())))
    # X, Y = init()



if __name__ == '__main__':
    print("Laboratoria 10 - tensorflow \n")

    preform_sgd()
