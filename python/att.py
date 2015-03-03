class G(object):
    def __init__(self):
        self.x = 88
        self.__x = 77

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if val == 0:
            raise Exception, 'cero no'
        self.__x = val

class F(object):
    def __init__(self):
        self.x = 88
        self.__x = 77

    def __setX(self, v):
        if v == 0:
            raise Exception, 'cero no'
        self.__x = v

    x = property(lambda self: self.__x, __setX)

class E(object):
    def __init__(self):
        self.x = 88
        self.__x = 77

    def __setX(self, v):
        if v == 0:
            raise Exception, 'cero no'
        self.__x = v

    def __getX(self):
        return self.__x

    x = property(fget = __getX, fset = __setX)

class D(object):
    def __init__(self):
        self.x = 88
        self.__x = 77

    def setX(self, v):
        if v == 0:
            raise Exception, 'cero no'
        self.__x = v

    def getX(self):
        return self.__x

    x = property(*(getX, setX))

class C(object):
    def __init__(self):
        self.x = 88
        self.__x = 77

    def setX(self, v):
        if v == 0:
            raise Exception, 'cero no'
        self.__x = v

    def getX(self):
        return self.__x

    x = property(**{'fset':setX, 'fget':getX})

if __name__ == '__main__':
    g = G()
    f = F()
    e = E()
    d = D()
    c = C()
    print c.x, d.x, e.x, f.x, g.x
    c.setX('duck typing')
    d.setX([3,5,7])
    f.x = .89
    g.x = bytearray('duck typing')

    f._F__x = 'realmente no soy privado'
    e._E__x = 'pero utilizame'

    print c.x, d.x, e.x, f.x, g.x

    e._E__setX('utilizame siempre que puedas')
    print c.x, d.x, e.x, f.x, g.x
