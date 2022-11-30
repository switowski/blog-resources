from string import Template

FIRST = "Sebastian"
LAST = "Witowski"
AGE = 33


def old_style():
    return "Hello %s %s (%i)" % (FIRST, LAST, AGE)


def template_strings():
    return Template("Hello ${first} ${last} (${age})").substitute(first=FIRST, last=LAST, age=AGE)


def new_style():
    return "Hello {} {} ({})".format(FIRST, LAST, AGE)


def f_strings():
    return f"Hello {FIRST} {LAST} ({AGE})"


def old_style_inline():
    return "Hello %s %s (%i)" % ("Sebastian", "Witowski", 33)
