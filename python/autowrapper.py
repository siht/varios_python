# -*- coding: cp1252 -*-
# fechad de inicio ?? Enero 2014
# fecha de lanzamiento 23 enero 2014
## author: José Carlos Tzompantzi de Jesús
## license: LGPL v3
## si no recibiste copia de la licencia ir a http://www.gnu.org/licenses/lgpl.html
## queda a disposición de quien quiera ocuparla y modificarla
## no hay garantía de que funcione, ni me hago responsable del uso potencial
## de este código
maths = '__add__', '__and__', '__div__', '__floordiv__', '__invert__', '__lshift__', '__mod__', '__mul__', '__neg__', '__or__', '__radd__', '__rand__', '__rdiv__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__sub__', '__truediv__', '__xor__'


def metodo(name):
    # esta función es externa, ya que no se me permite incluirla en la definición de una metaclase
    # además de que el truco con funciones lambda no me funcionó
    if name in maths:
        a = 'def {0}(self, *args, **kwargs):\n    return self.__class__(self.wrap.{0}(*args, **kwargs))\nwrap_method = {0}\ndel({0})\n'.format(name)
    else:
        a = 'def {0}(self, *args, **kwargs):\n    return self.wrap.{0}(*args, **kwargs)\nwrap_method = {0}\ndel({0})\n'.format(name)
    exec(a)
    method = wrap_method
    del(wrap_method)
    return method

def propiedad(name):
    # igual esta que la anterior
    a = '''def setter(self, value):
    self.wrap.{0} = value
def getter(self):
    return self.wrap.{0}'''.format(name)
    exec(a)
    ret = property(getter, setter)
    del(setter, getter)
    return ret

class MetaWrap(type):
    # métodos que no quiero sobreescribir
    invalid = ('__init__', '__new__', '__subclasshook__', '__class__', '__str__',
               '__delattr__', '__getattribute__', '__setattr__', '__repr__', '__doc__', 'wrap')
    # diccionario para obtener por clase los métodos a sobre escribir
    # todo:poner uno de referencias débiles
    _clss = {}
    def __init__(cls, name, bases, dct):
        # esta parte se encarga de revisar que atributos se sobreescribirán
        over_dct = {} # auxiliar
        over = [method for method in dct if not method.startswith('__')] # obtener métodos a sobre escribir (aqui de hecho son todos los atributos)
        for m in over:
            over_dct[m] = dct[m]
        # si una clase se construyó con este constructor queda registrada para hacer bien la sobreescritura de
        # los métodos, aquí recomiendo poner el id de la clase en lugar de su nombre, por que nunca se sabe con
        # los nombres de clase, algunos pueden repetirse incluso en el mismo namespace
        # y de paso no hago referencias circulares
        if id(cls) not in cls._clss: # este es por si hay herencia
            cls._clss[id(cls)] = over_dct
        super(MetaWrap, cls).__init__(name, bases, dct)

    def __call__(cls, *params, **kwparams):
        # obtener un parámetro o None si no hay
        kls = type(cls.__name__, (cls, ), {'__module__':cls.__module__}) # copia de la clase
        wrap = None
        if params:
            wrap = params[0]
        if not params and kwparams:
            wrap = kwparams.popitem()[1]
        # obtener todos los atributos del objeto
        obj_attrs = dir(wrap)
        id_cls = id(cls)
        for attr in obj_attrs:
            # verificar que no esté sobre escrito
            if attr not in cls._clss[id_cls]:
                # asignar métodos a la clase y hacer que los método tengan un valor por default
                if callable(wrap.__getattribute__(attr)) and attr not in cls.invalid:
                    setattr(cls, attr, metodo(attr))
                # asignar atributos pero todos como propiedades
                if not callable(attr) and attr not in cls.invalid and not attr.startswith('__'):
                    setattr(cls, attr, propiedad(attr))
        # crear el objeto
        obj = super(MetaWrap, cls).__call__()
        # y añadirle al vuelo el objeto a envolver
        obj.wrap = wrap
        return obj
        
        def __methodize(self, name):
            if name in maths:
                a = lambda self, *args, **kwargs, name=name: self.__class__(self.wrap.{0}(*args, **kwargs))
            else:
                a = lambda self, *args, **kwargs, name=name: self.wrap.{0}(*args, **kwargs)
                a = 'def {0}(self, *args, **kwargs):\n    return self.wrap.{0}(*args, **kwargs)\nwrap_method = {0}\ndel({0})\n'.format(name)
################################################################################################    
if __name__ == '__main__':
    ## algunos nombres no los he cambiado y es por una confusión de términos de mi parte entre
    ## Wrapper y Patrón Decorador, los he dejado así de momento
    
    class Decorador(object): __metaclass__ = MetaWrap

    class DecoSimple(Decorador):
        def inerte(self): pass # se comporta como mixin
        
        def mthod(self): # y ya puede 'sobre escribir' un método
            return self.wrap.mthod() - 66

    class DecoInt(Decorador): pass

    class ObjetoSimple(object):
        hola = 'je'
        def mthod(self):
            return 99

        def atributize(self, value):
            self.a = value

        def get_a(self):
            return self.a
    
    obj = ObjetoSimple()
    entero_decorado = DecoInt(5)
    entero_decorado *= 10
    print entero_decorado.wrap
    obj_decorado = DecoSimple(obj)
    print obj_decorado.mthod()
    obj_decorado.atributize('hola')
    print obj_decorado.get_a()
    print obj_decorado.inerte()
    print obj_decorado.hola
