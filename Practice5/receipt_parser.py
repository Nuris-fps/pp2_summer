import re

def ZeroOrMoreB():
    txt = input()
    x = re.findall("ab*", txt)
    print(x)
# ZeroOrMoreB()
# zero or more "b" following "a"

def TwoOrThree():
    txt = input()
    x = re.findall("ab{2,3}", txt)
    print(x)
# TwoOrThree()
# two or three "b" following "a"

def sequenceOfLowerLetters():
    txt = input()
    l = []
    pattern = r'^[a-z]+_[a-z]+$'
    words = txt.split()
    matches = [w for w in words if re.match(pattern, w)]
    print(matches)
sequenceOfLowerLetters()

def findAa():
    txt = input()
    x = re.findall("[A-Z][a-z]+", txt)
    print(x)
# findAa()

def startWithAEndWithB():
    txt = input()
    x = re.findall("^a.*b$", txt)
    print(x)
# startWithAEndWithB()

def replace():
    txt = input()
    x = txt
    # pattern = ",. "
    x = re.sub(r"\s", ":", txt)
    x = re.sub(r"[.]", ":", x)
    x = re.sub(r",", ":", x)
# replace()

def snakeToCamel():
    txt = input()
    x = txt.split("_")
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    for x in x:
        print(x, end='')
# snakeToCamel()

def splitUpper():
    txt = input()
    x = txt
    for i in range(0, len(x)):
        if x[i].isupper():
            x1 = x[:i]
            x2 = x[i + 1:]
            x = x1 + ' ' + x2
    # l = x.split(' ')
    l = re.split(r"\s", x)
    l2 = []
    for i in l:
        if len(i) != 0:
            l2.append(i)
    print(l) # if AskarOralkhan [ [], 'skar', 'ralkhan' ]
    print(l2)
# splitUpper()

def splitUpper2():
    txt = input()
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    print(x)
# splitUpper2()

def camelToSnake():
    txt = input()    
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    # camelCase
    # print(x)
    # camel Case
    x = x.split(' ')
    s = ''
    for i in range(0, len(x)):
        s += x[i].lower() + '_'
    print(s[:-1]) # deleting last character
camelToSnake()