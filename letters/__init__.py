import check50
import check50.c
from pathlib import Path

@check50.check()
def exists():
    """letters.c exists"""
    check50.exists("letters.c")
    check50.include("case1.txt", "case2.txt", "case3.txt", "case4.txt", "case5.txt")


@check50.check(exists)
def compiles():
    """letters.c compiles"""
    check50.c.compile("letters.c", lcs50=True)


@check50.check(compiles)
def test83():
    """WORD"""
    io = split_test_io("case1.txt")
    out = check50.run("./letters").stdin(io['in']).stdout(io['out'])
    compare_outputs(8, 3, out)


def split_test_io(filename):
    str = Path(filename).read_text()
    dict = {}

    dict['in'] = str[str.index("phrase: ")+8:str.index("\n", str.index("phrase: "))]
    dict['out'] = str[str.index("\n"):].rstrip("\n")

    return dict

def compare_outputs(filename, stdout):
    output = "floored letters: " + str(dividend // divisor) + "\n"
    output += "remainder: " + str(dividend % divisor) + "\n"
    output += "letters: " + '{:.3f}'.format(round(dividend/divisor, 3))

    if output == stdout.lower().rstrip("\n"):
        return

    raise check50.Mismatch(output, stdout)

