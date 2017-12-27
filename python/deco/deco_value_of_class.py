class locker:
    def __int__(self):
        print ("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called. (this is static method )")

    @staticmethod
    def release():
        print ("   locker.release() called. (no need object instance)")


def deco(cls):
    '''cls must achieve acquire and release'''
    def _deco(func):
        def __deco():
            print ("before %s called [%s]." %(func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()

        return __deco
    return _deco

@deco(locker)
def myfunc():
    print ("myfunc() called.")

myfunc()
