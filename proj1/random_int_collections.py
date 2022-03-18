from numpy import random, array


# i.
# gerar uma colecção aleatória de inteiros numa lista
# inteiros devem pertencer ao intervalo [1, 1000000]

# ! o enunciado não diz quantos inteiros devem ser !

def generate_random_int_list(length):
    int_list = []
    for i in range(length):
        int_list.append(random.random_integers(1, 1000000))
    return int_list

def generate_random_int_array(length):
    return random.randint(1, 1000000, size=length)