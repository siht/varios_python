# -*- coding: cp1252 -*-
class Typer(type):
    def __new__(cls, name, bases, dct):
        '''este si regresa una instancia(en este caso una clase), esta parte construye la clase
            y por supuesto, sólo se llama una sola vez (la clase se construye una sola vez)
            este método se modifica para que las clases que implementen esta metaclase
            puedan escribir los atributos que no se pueden modificar una vez creada la clase,
            agregar mas clases bases (o quitarlas)
            agregar atributos de clase
            imposibilitar la agregacion de atributos a la clase, etc
        '''
        print 'new====================='
        print '=====================name\n', name
        print '=====================bases\n', bases
        print '=====================dct\n', dct
        print '=====================cls.__name__\n', cls.__name__
        print '=====================cls.__dict__\n', cls.__dict__
        a = type.__new__(cls, name, bases, dct)
        print 'return\n', a
        return a

    def __init__(cls, name, bases, dct):
        '''este no devuelve valor alguno (mas que None), sirve sólo para inicializar valores de clase
            y obviamente (ese obviamente es para los que si saben leer -yo no, yo si hize la prueba-)
            se llama una sola vez.
        '''
        print '\n\ninit====================='
        print '=====================name\n', name
        print '=====================bases\n', bases
        print '=====================dct\n', dct
        print '=====================cls.__name__\n', cls.__name__
        print '=====================cls.__dict__\n', cls.__dict__
##        a = type.__init__(cls, name, bases, dct)
##        print 'return\n', a  ## imprime return<br> None
    
    def __call__(cls, obj):
        '''este es llamado cada vez que la clase es instanciada
            este si recibe los parámetros de creación de instancias
            '''
        print '\n\ncall====================='
        print cls
        print obj
        print '=====================cls.__name__\n', cls.__name__
        print '=====================cls.__dict__\n', cls.__dict__
        a = type.__call__(cls, obj)
        print 'return\n', a
        return a

class O(object):
    def jojuy(self):
        pass

    def __Joseeg(self):
        pass

    def _loro(self):
        pass

class P(object):
    __metaclass__ = Typer
    def __init__(self, obj):
        self.o = obj

o = O()
p = P(o)
b = P(o)


class Wrapper(object):
    def __init__(self, obj):
        self.__im = "_" + obj.__class__.__name__
        self.methodList = \
        [
            method
            for method in dir(o)
            if callable(getattr(o, method)) and
            not method.startswith('__') and
            not method.startswith(self.__im)
        ]

o=O()
w = Wrapper(o)
print
print w.methodList
