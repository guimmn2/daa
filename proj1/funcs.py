import numpy
from numpy import random as r
from timeit import repeat


# i.
# gerar uma colecção aleatória de inteiros numa lista
# inteiros devem pertencer ao intervalo [1, 1000000]

# ! o enunciado não diz quantos inteiros devem ser !

def generate_random_int_list(length):
    int_list = []
    for i in range(length):
        int_list.append(r.random_integers(1, 100000))
    return int_list


def generate_random_int_array(length):
    return r.randint(1, 100000, size=length)


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

def search_bin(collection, val):
    if isinstance(collection, list):
        collection.sort()
        return binarySearch(collection, 0, len(collection), val)

    elif isinstance(collection, numpy.ndarray):
        sorted = numpy.sort(collection)
        return binarySearch(sorted, 0, sorted.size, val)

#devolve duração média dada uma lista de durações
def get_avg_duration(search_func, nr_of_calls):
    duration_list = repeat(lambda: search_func, number=1, repeat=nr_of_calls)
    return sum(duration_list)/len(duration_list)

def get_random_item_of(collection):
    return r.randint(0, len(collection))

### Binary Search implementation
def binarySearch(arr, start, size, x):
    if size >= 1:

        mid = (start + ( size - 1 )) // 2
        if mid == arr[mid]:
            return  mid

        if arr[mid] > x:
            binarySearch(arr, start, mid - 1, x)
        else:
            binarySearch(arr, mid + 1, size, x)
    else:
        return -1