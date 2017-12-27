def deco(func):
    def _newfunc(*args,**kwargs):
        print ('before %s called.'%func.__name__)
        ret = func(*args, **kwargs)
        print ('after %s called. resul: %s'%(func.__name__, ret))
        return ret
    return _newfunc

@deco
def myfunc(a,b=8,c=1):
    print ('myfunc2(%s,%s,%s) called.'%(a,b,c))
    return a+b+c

myfunc(1)
myfunc(1,4)
myfunc(1,10,9)
