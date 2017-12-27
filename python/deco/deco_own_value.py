import functools

def deco(arg):
    def _deco(func):
      ##  @functools.wraps(func) save myfunc original name
        def _newfunc():
            print ("before %s called [%s]." %(func.__name__,arg))
            func()
            print("after %s called [%s]." %(func.__name__, arg))
        return _newfunc
    return _deco

@deco("mymodule")
def myfunc():
    print("myfunc() called.")


myfunc()
print myfunc.__name__
