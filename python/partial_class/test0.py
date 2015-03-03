from partial import Partial

class One(object):
    __metaclass__ = Partial
    def __init__(self):
        self.__attr = 9

class One(object):
    __metaclass__ = Partial
    def one_method(self):
        return self.__attr

class One(object):
    __metaclass__ = Partial
    def __repr__(self):
        return 'Class One'

class Two(object):
     __metaclass__ = Partial

if __name__ == '__main__':
    o = One()
    t = Two()
    print o
    print t
    print o.one_method()