import numpy
from numpy import random


# i.
# gerar uma colecção aleatória de inteiros numa lista
# inteiros devem pertencer ao intervalo [1, 1000000]

# ! o enunciado não diz quantos inteiros devem ser !

def generate_random_int_list(length):
    int_list = []
    for i in range(length):
        int_list.append(random.random_integers(1, 10))
    return int_list


def generate_random_int_array(length):
    return random.randint(1, 10, size=length)


# 2

def search_in(collection, val):
    if isinstance(collection, list):
        if val in collection:
            return collection.index(val)
        else:
            return -1
    elif isinstance(collection, numpy.ndarray):
        if val in collection:
            return numpy.argmax(collection == val)
    else:
        return -1
