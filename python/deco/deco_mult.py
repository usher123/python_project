class mylocker:
    def _init_(self):
        print ("mylocker._init_() called.")

    @staticmethod
    def acquire():
        print ("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print ("   mylocker.unlock() called.")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print ("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")

def lockhelper(cls):
    '''cls must achieve the both staticmethod of acquire and release'''
    def _deco(func):
        def __deco(*args, **kwargs):
            print ("beford %s called." %func.__name__)
            cls.acquire()
            try:
                return func(*args , **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco


class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print("myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print (" myfunc2() called.")
        return a + b

a = example()
a.myfunc()
print (a.myfunc())
print (a.myfunc2(1,2))
print (a.myfunc2(3,4))

