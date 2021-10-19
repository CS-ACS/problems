import check50
import check50.c
from random import randint

@check50.check()
def exists():
    """quotient.c exists"""
    check50.exists("quotient.c")


@check50.check(exists)
def compiles():
    """quotient.c compiles"""
    check50.c.compile("quotient.c", lcs50=True)


@check50.check(compiles)
def test83():
    """input of 8 and 3 yields output of 2, 2, and 2.667"""
    out = check50.run("./quotient").stdin("8").stdin("3").stdout()
    compare_outputs(8, 3, out)

@check50.check(compiles)
def test93():
    """input of 9 and 3 yields output of 3, 0, and 3.000"""
    out = check50.run("./quotient").stdin("9").stdin("3").stdout()
    compare_outputs(9, 3, out)

@check50.check(compiles)
def test324():
    """input of 99 and 25 yields output of 3, 24, and 3.960"""
    out = check50.run("./quotient").stdin("99").stdin("25").stdout()
    compare_outputs(99, 25, out)

@check50.check(compiles)
def test1999():
    """input of 1 and 999 yields output of 0, 1, and 0.001"""
    out = check50.run("./quotient").stdin("1").stdin("999").stdout()
    compare_outputs(1, 999, out)

@check50.check(compiles)
def testrand1():
    """input of random numbers yields the correct output (1)"""
    dividend = randint(1, 999)
    divisor = randint(1, dividend)

    out = check50.run("./quotient").stdin(str(dividend)).stdin(str(divisor)).stdout()
    compare_outputs(dividend, divisor, out)

@check50.check(compiles)
def testrand2():
    """input of random numbers yields the correct output (2)"""
    divisor = randint(1, 999)
    dividend = randint(1, divisor)

    out = check50.run("./quotient").stdin(str(dividend)).stdin(str(divisor)).stdout()
    compare_outputs(dividend, divisor, out)

@check50.check(compiles)
def testrand3():
    """input of random numbers yields the correct output (3)"""
    divisor = randint(1, 999)
    dividend = randint(1, 999)

    out = check50.run("./quotient").stdin(str(dividend)).stdin(str(divisor)).stdout()
    compare_outputs(dividend, divisor, out)


def compare_outputs(dividend, divisor, stdout):
    output = "floored quotient: " + str(dividend // divisor) + "\n"
    output += "remainder: " + str(dividend % divisor) + "\n"
    output += "quotient: " + '{:.3f}'.format(round(dividend/divisor, 3))

    if output == stdout.rstrip("\n"):
        return

    raise check50.Mismatch(output, stdout)

