# -*- coding: cp1252 -*-


# esto es un comentario
## y esto también
## pero la primera línea no es un comentario
##
## Autor José Carlos Tzompantzi (aka negativo)
## este pedazo de código no sirve de mucho pero bueno, es un ejemplo
## fecha 16/11/2013
##
##
## ejemplo de como agregar una herencia automática después de haber definido
## la clase mediante un decorador.
## en este caso la clase A tiene un decorador de tipo función que agrega a modo
## de herencia, IClass (ojo, en python no existe tal cosa como una interfaz pero,
## tiene herencia múltiple, pero tomando buenas prácticas de programación,
## podemos hacer que esa clase se comporte a manera de interfaz) de la cual
## hereda una variable(si, no es el comportamiento de una interfaz, pero aplica)


## esta función va a trabajar a modo de decorador y va a "inyectar" herencia
## a una clase ya creada
def agregar_interface(C): #así se define una función
    """ este es un pydoc similar al javadoc, solo que se pone como un string
        multilinea
        agrega una clase ya predefinida a otra clase
    """
    ##########################################################################
    class IClass(object): # definimos una clase interna
        # los métodos se definen con la misma sintaxis que una funcion
        def __init__(self): # self va por fuerza en un método (es el "this")
            self._x = 666 # un atributo de clase "privado" (lo cual no existe)

        @property #decorador para hacer de un método una propiedad
        def x(self):
            return self._x
    ##########################################################################

    # la función type tiene dos usos, pero aquí nos centraremos a que es una
    # "fábrica" de clases. A la variable 'X' le asignamos una nueva clase
    # la cual se llama igual que la clase que entró como parámetro
    # nota antes de continuar:
    # C.__name__ devuelve el nombre de la clase que lo definió
    #
    # continuamos
    # entonces este type tiene 3 parámetros
    # 1.- nomre de la clase a crear
    # 2.- una lista (de hecho ese párametro no es de tipo lista pero,
    # intencionalmente lo voy a llamar así en este ejemplo -su nombre real es
    # tupla-) de las clases de las cuales hereda en este caso de C y de IClass
    # 3.- y un diccionario de atributos y métodos de esa nueva clase, en este
    # caso está vacio, ya que va a tomarlos de las clases heredadas
    X = type(C.__name__, (C, IClass), {})
    return X # y regresamos de nuevo esa clase pero con una "herencia inyectada"


##############################################################
@agregar_interface # la función de arriba aplicada a manera de decorador
class A(object):
    d = 0 # también así se pueden agregar atributos

##############################################################
# no existe un método main pero este truco es útil
# es mas, no es necesario el main
if __name__ == '__main__': # si quieren quitar este if dedenten las líneas posteriores
    print A
    a= A()
    print a.d, a.x
    a.z = 777 # y también se puede agregar atributos y métodos al vuelo
    print a.z
