def deco(func):
    def _newfunc(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("after myfunc() called. result: %s" % ret)
        return ret
    return _newfunc

@deco
def myfunc(a, b):
    print("myfunc(%s,%s) called." % (a, b))
    return a + b

myfunc(1, 2)

b=deco(myfunc(2,3))
