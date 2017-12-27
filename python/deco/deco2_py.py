def deco(func):
    def _newfunc():
        print("before myfunc() called.")
        a =func()
        print("after myfunc() called.")# no need to return func,actually  return value of  the orignal function
        print a 
    return _newfunc

@deco
def myfunc():
    print("myfunc() called.")
    return 'ok'

a = myfunc()
print a
