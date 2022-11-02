class BaseClass:
    hello = "world"
    bar = "world"
    baz = "world"

class Foo(BaseClass):
    pass

FOO = Foo()

# Look before you leap
def test_permission2():
    if hasattr(FOO, "hello") and hasattr(FOO, "bar") and hasattr(FOO, "baz"):
        FOO.hello
        FOO.bar
        FOO.baz

# Ask for forgiveness
def test_forgiveness2():
    try:
        FOO.hello
        FOO.bar
        FOO.baz
    except AttributeError:
        pass
