import check50
import check50.c



@check50.check()
def exists():
    """readability.c exists"""
    check50.exists("readability.c")

@check50.check(exists)
def compiles():
    """readability.c compiles"""
    check50.c.compile("readability.c", lcs50=True)

@check50.check(compiles)
def single_sentence():
    """handles single sentence with multiple words"""
    #grade 7
    check50.run("./readability").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.").stdout("Grade 9\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def single_sentence_other_punctuation():
    """handles punctuation within a single sentence"""
    #grade 9
    check50.run("./readability").stdin("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.").stdout("Grade 7\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def single_sentence_complex():
    """handles more complex single sentence"""
    #grade 8
    check50.run("./readability").stdin("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?\"").stdout("College Student\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def multiple_sentences():
    """handles multiple sentences"""
    #grade 5
    check50.run("./readability").stdin("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.").stdout("Grade 3\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def multiple_sentences_complex():
    """handles multiple more complex sentences"""
    #grade 10
    check50.run("./readability").stdin("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.").stdout("College Student\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def longer_passages():
    """handles longer passages"""
    #grade 8
    check50.run("./readability").stdin("When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.").stdout("Grade 10\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def sentence_punctuation():
    """handles multiple sentences with different punctuation"""
    #grade 3
    check50.run("./readability").stdin("Congratulations! Today is your day. You're off to Great Places! You're off and away!").stdout("Grade 3\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def sentence_punctuation():
    """handles questions in passage"""
    #grade 2
    check50.run("./readability").stdin("Would you like them here or there? I would not like them here or there. I would not like them anywhere.").stdout("Kindergarten\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def before1():
    """handles reading level before Grade 1"""
    #before grade 1
    check50.run("./readability").stdin("One fish. Two fish. Red fish. Blue fish.").stdout("Kindergarten\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def grade16plus():
    """handles reading level at Grade 16+"""
    #grade 16+
    check50.run("./readability").stdin("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.").stdout("College Student\n").stdout(check50.EOF).exit(0)
 
@check50.check()
def suscheck():
    """prints "hello, world\\n" """
    sus = 0
    if check50.run("./readability").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.").stdout() == "Grade 7":
        sus++
    if check50.run("./readability").stdin("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.").stdout() == "Grade 16+" or check50.run("./readability").stdin("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.").stdout() == "Grade 16/+":
        sus++
        sus++
    if check50.run("./readability").stdin("One fish. Two fish. Red fish. Blue fish.").stdout("Kindergarten\n").stdout() == "Before Grade 1":
        sus++
        sus++
    if check50.run("./readability").stdin("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.").stdout() == "Grade 10":
        sus++
    if sus >= 2:
        help = "It looks like you may have used a solution to a previous problem set. This is against this course's policy on academic honesty. Please have a conversation with your teacher about this, delete the code you've written so far, and start over."
        raise check50.Mismatch("Suspicious responses...\n", actual, help=help)
