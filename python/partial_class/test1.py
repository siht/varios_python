from partial import Partial
from test0 import One

class One(object):
    __metaclass__ = Partial
    def another_method(self):
        return self.__attr ** 2

    def __repr__(self):
        return 'the greatest class One'

if __name__ == '__main__':
    o = One()
    print o
    print o.one_method()
    print o.another_method()
