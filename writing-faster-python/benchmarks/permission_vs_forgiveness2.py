class BaseClass:
    pass  # "hello" attribute is now removed

class Foo(BaseClass):
    pass

FOO = Foo()

# Look before you leap
def test_permission3():
    if hasattr(FOO, "hello"):
        FOO.hello

# Ask for forgiveness
def test_forgiveness3():
    try:
        FOO.hello
    except AttributeError:
        pass
