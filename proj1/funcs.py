import numpy
from numpy import random
from timeit import repeat


# i.
# gerar uma colecção aleatória de inteiros numa lista
# inteiros devem pertencer ao intervalo [1, 1000000]

# ! o enunciado não diz quantos inteiros devem ser !

def generate_random_int_list(length):
    int_list = []
    for i in range(length):
        int_list.append(random.random_integers(1, 100000))
    return int_list


def generate_random_int_array(length):
    return random.randint(1, 100000, size=length)


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

#devolve lista com durações das várias chamadas
def get_durations(search_func, nr_of_calls):
    return repeat(lambda: search_func, number=1, repeat=nr_of_calls)

#devolve duração média dada uma lista de durações
def get_avg_duration(duration_list: list):
    return sum(duration_list)/len(duration_list)