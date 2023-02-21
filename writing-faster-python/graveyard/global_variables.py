C = 1

def local_var():
    a = 1
    return sum(a for _ in range(1_000_001))

def nested():
    b = 1
    def fn():
        return sum(b for _ in range(1_000_001))
    return fn()

def global_var():
    return sum(C for _ in range(1_000_001))

def built_in():
    return [list() for _ in range(1_000_001)]


########################

C2 = list

def local_var2():
    a = list
    return a

def nested2():
    b = list
    def fn():
        return b
    return fn()

def global_var2():
    return C2

def built_in2():
    return list


#########################

from pathlib import Path

oldlist = Path("/usr/share/dict/words").read_text().splitlines()
# oldlist now contains 2493885 words

def initial():
    newlist = []
    for word in oldlist:
        newlist.append(word.upper())
    return newlist

def local_variables():
    upper = str.upper
    newlist = []
    append = newlist.append
    for word in oldlist:
        append(upper(word))
    return newlist

def comprehension():
    return [word.upper() for word in oldlist]

def a_map():
    return list(map(str.upper, oldlist))
