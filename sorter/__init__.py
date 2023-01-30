import check50
from random import randint

@check50.check()
def exists():
    """credit.py exists."""
    check50.exists("sorter.py")

@check50.check(exists)
def bubble1():
    """Bubble Sort"""
    arr = generate_list()
    instr = "python3 sorter.py " + " ".join(arr)
    answer = bubble_sort(arr)
    check50.run(instr).stdin(instr).stdout(answer.strip()).exit()

@check50.check(exists)
def bubble2():
    """Bubble Sort 2"""
    arr = generate_list()
    instr = "python3 sorter.py " + " ".join(arr)
    answer = bubble_sort(arr)
    check50.run(instr).stdin(instr).stdout(answer.strip()).exit()

@check50.check(exists)
def selection1():
    """Selection Sort"""
    arr = generate_list()
    instr = "python3 sorter.py " + " ".join(arr)
    answer = selection_sort(arr)
    check50.run(instr).stdin(instr).stdout(answer.strip()).exit()

@check50.check(exists)
def selection2():
    """Selection Sort 2"""
    arr = generate_list()
    instr = "python3 sorter.py " + " ".join(arr)
    answer = selection_sort(arr)
    check50.run(instr).stdin(instr).stdout(answer.strip()).exit()

@check50.check(exists)
def insertion1():
    """Insertion Sort"""
    arr = generate_list()
    instr = "python3 sorter.py " + " ".join(arr)
    answer = insertion_sort(arr)
    check50.run(instr).stdin(instr).stdout(answer.strip()).exit()

@check50.check(exists)
def insertion2():
    """Insertion Sort 2"""
    arr = generate_list()
    instr = "python3 sorter.py " + " ".join(arr)
    answer = insertion_sort(arr)
    check50.run(instr).stdin(instr).stdout(answer.strip()).exit()

def generate_list():
    return [str(randint(0, 50)) for i in range(randint(5, 20))]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def bubble_sort(l):
    output = ""
    length = len(l)
    while not issorted(l):
        for i in range(length-1):
            if l[i] > l[i+1]:
                swap(l, i, i+1)
                output += str(l) + "\n"
    return output

def selection_sort(l):
    output = ""
    while not issorted(l):
        for i in range(len(l)):
            minv = min(l[i:])
            mini = l[i:].index(minv)
            if mini+i != i:
                swap(l, i, mini+i)
                output += str(l) + "\n"
    return output

def insertion_sort(l, quieter=False):
    output = ""
    while not issorted(l):
        for i in range(1, len(l)):
            j = i
            while l[j] < l[j-1] and j > 0:
                swap(l, j, j-1)
                if not quieter:
                    output += str(l) + "\n"
                j -= 1
            if quieter and i != j:
                output += str(l) + "\n"

def issorted(l):
    if all(l[i] <= l[i+1] for i in range(len(l) - 1)):
        return True
    return False