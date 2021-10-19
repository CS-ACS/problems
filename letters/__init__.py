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
def testWORD():
    """WORD"""
    io = split_test_io("case1.txt")
    out = check50.run("./letters").stdin(io['in']).stdout(io['out'])

@check50.check(compiles)
def testTWO():
    """TWO words!"""
    io = split_test_io("case2.txt")
    out = check50.run("./letters").stdin(io['in']).stdout(io['out'])

@check50.check(compiles)
def testaeroplane():
    """in the aeroplane over the sea"""
    io = split_test_io("case3.txt")
    out = check50.run("./letters").stdin(io['in']).stdout(io['out'])

@check50.check(compiles)
def testamerican():
    """the last great american dynasty"""
    io = split_test_io("case4.txt")
    out = check50.run("./letters").stdin(io['in']).stdout(io['out'])

@check50.check(compiles)
def teststrangelove():
    """Dr. Strangelove or: how I learned to stop worrying and love the bomb"""
    io = split_test_io("case5.txt")
    out = check50.run("./letters").stdin(io['in']).stdout(io['out'])

def split_test_io(filename):
    str = Path(filename).read_text()
    dict = {}

    dict['in'] = str[str.index("phrase: ")+8:str.index("\n", str.index("phrase: "))]
    dict['out'] = str[str.index("\n")+1:].rstrip("\n")

    return dict

