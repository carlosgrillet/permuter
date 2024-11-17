import itertools
import math


def num_of_perms(elements: int) -> int:
    '''Calculate the number of permutations of a given number of elements
    :param elements: int: Number of elements to be permute
    '''
    perms = 0
    for word_length in range(2, elements + 1):
        perms += math.perm(elements, word_length)

    return perms


def iterate_elemets(data: list, minimum_word_length: int) -> list:
    return [
        ''.join(value) + "\n"
        for word_length in range(2, len(data) + 1)
        for value in itertools.permutations(data, word_length)
    ]
