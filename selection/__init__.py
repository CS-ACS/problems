import check50
import check50.c
from random import randint
import sys
from numpy import *

@check50.check()
def exists():
    """selection.c exists"""
    check50.exists("selection.c")
    

@check50.check(exists)
def compiles():
    """selection.c compiles"""
    check50.c.compile("selection.c", lcs50=True)


@check50.check(compiles)
def no_arguments():
    """returns error if no arguments"""
    out = check50.run("./selection").stdout()

    if "usage:" not in out.lower():
        raise check50.Mismatch("Usage: ./selection [int 1], [int 2] ...", out, )


@check50.check(compiles)
def one_argument():
    """behaves correctly when given only 1 argument"""
    check50.run("./selection 50").stdout("50")


@check50.check(compiles)
def one_argument():
    """behaves correctly when given 2 arguments"""
    check50.run("./selection 50, 5").stdout("5 50\n5 50")


@check50.check(compiles)
def testrand1():
    """behaves correctly when given a random number of random numbers"""
    io_tuple = generate_input()
    answer = io_tuple[1]
    inputs = "./selection " + ' '.join(str(e) for e in io_tuple[0])

    check50.run(inputs).stdout(answer)


@check50.check(compiles)
def testrand2():
    """behaves correctly when given a random number of random numbers"""
    io_tuple = generate_input()
    answer = io_tuple[1]
    inputs = "./selection " + ' '.join(str(e) for e in io_tuple[0])

    check50.run(inputs).stdout(answer)


@check50.check(compiles)
def testrand3():
    """behaves correctly when given a random number of random numbers"""
    io_tuple = generate_input()
    answer = io_tuple[1]
    inputs = "./selection " + ' '.join(str(e) for e in io_tuple[0])

    check50.run(inputs).stdout(answer)


def generate_input():
    inputs = []
    num_inputs = randint(4, 10) // 2

    for i in range(num_inputs):
        n = randint(0, 499)
        inputs.append(n)
        n = randint(500, 1000)
        inputs.append(n)

    outputs = inputs.copy()
    return (inputs, selection_sort(outputs))


def selection_sort(A):
# Traverse through all array elements
    outputs = []
    for i in range(len(A)):
         
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                 
        # Swap the found minimum element with
        # the first element       
        if i != min_idx:
            A[i], A[min_idx] = A[min_idx], A[i]
            outputs.append(' '.join(str(e) for e in A))

    return '\n'.join(e for e in outputs) + "\n"