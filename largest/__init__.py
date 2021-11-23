import check50
import check50.c
from random import randint

@check50.check()
def exists():
    """largest.c exists"""
    check50.exists("largest.c")

@check50.check(exists)
def compiles():
    """largest.c compiles"""
    check50.c.compile("largest.c", lcs50=True)

@check50.check(compiles)
def no_arguments():
    """returns error if no arguments"""
    out = check50.run("./largest").stdout()

    if "usage:" not in out.lower():
        raise check50.Mismatch("Usage: ./largest [int 1], [int 2] ...", out, )


@check50.check(compiles)
def one_argument():
    """behaves correctly when given only 1 argument"""
    check50.run("./largest 50").stdout("50")

@check50.check(compiles)
def one_argument():
    """behaves correctly when given 2 arguments"""
    check50.run("./largest 50, 5").stdout("50")

@check50.check(compiles)
def testrand1():
    """behaves correctly when given a random number of random numbers"""
    io_tuple = generate_input()
    answer = io_tuple[1]
    inputs = "./largest " + ' '.join(str(e) for e in io_tuple[0])

    check50.run(inputs).stdout(answer)

    @check50.check(compiles)
def testrand2():
    """behaves correctly when given a random number of random numbers"""
    io_tuple = generate_input()
    answer = io_tuple[1]
    inputs = "./largest " + ' '.join(str(e) for e in io_tuple[0])

    check50.run(inputs).stdout(answer)

@check50.check(compiles)
def testrand3():
    """behaves correctly when given a random number of random numbers"""
    io_tuple = generate_input()
    answer = io_tuple[1]
    inputs = "./largest " + ' '.join(str(e) for e in io_tuple[0])

    check50.run(inputs).stdout(answer)


def generate_input():
    inputs = []
    num_inputs = randint(3, 20)

    for i in range(num_inputs):
        n = randint(-1000, 1000)
        inputs.append(n)

    return (inputs, max(inputs))



def compare_outputs(output):
    output = "floored quotient: " + str(dividend // divisor) + "\n"
    output += "remainder: " + str(dividend % divisor) + "\n"
    output += "quotient: " + '{:.3f}'.format(round(dividend/divisor, 3))

    if output.rstrip("\n") == stdout.lower().rstrip("\n"):
        return

    raise check50.Mismatch(output, stdout)

