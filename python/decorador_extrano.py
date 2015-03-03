# -*- coding: cp1252 -*-


# esto es un comentario
## y esto tambi�n
## pero la primera l�nea no es un comentario
##
## Autor Jos� Carlos Tzompantzi (aka negativo)
## este pedazo de c�digo no sirve de mucho pero bueno, es un ejemplo
## fecha 16/11/2013
##
##
## ejemplo de como agregar una herencia autom�tica despu�s de haber definido
## la clase mediante un decorador.
## en este caso la clase A tiene un decorador de tipo funci�n que agrega a modo
## de herencia, IClass (ojo, en python no existe tal cosa como una interfaz pero,
## tiene herencia m�ltiple, pero tomando buenas pr�cticas de programaci�n,
## podemos hacer que esa clase se comporte a manera de interfaz) de la cual
## hereda una variable(si, no es el comportamiento de una interfaz, pero aplica)


## esta funci�n va a trabajar a modo de decorador y va a "inyectar" herencia
## a una clase ya creada
def agregar_interface(C): #as� se define una funci�n
    """ este es un pydoc similar al javadoc, solo que se pone como un string
        multilinea
        agrega una clase ya predefinida a otra clase
    """
    ##########################################################################
    class IClass(object): # definimos una clase interna
        # los m�todos se definen con la misma sintaxis que una funcion
        def __init__(self): # self va por fuerza en un m�todo (es el "this")
            self._x = 666 # un atributo de clase "privado" (lo cual no existe)

        @property #decorador para hacer de un m�todo una propiedad
        def x(self):
            return self._x
    ##########################################################################

    # la funci�n type tiene dos usos, pero aqu� nos centraremos a que es una
    # "f�brica" de clases. A la variable 'X' le asignamos una nueva clase
    # la cual se llama igual que la clase que entr� como par�metro
    # nota antes de continuar:
    # C.__name__ devuelve el nombre de la clase que lo defini�
    #
    # continuamos
    # entonces este type tiene 3 par�metros
    # 1.- nomre de la clase a crear
    # 2.- una lista (de hecho ese p�rametro no es de tipo lista pero,
    # intencionalmente lo voy a llamar as� en este ejemplo -su nombre real es
    # tupla-) de las clases de las cuales hereda en este caso de C y de IClass
    # 3.- y un diccionario de atributos y m�todos de esa nueva clase, en este
    # caso est� vacio, ya que va a tomarlos de las clases heredadas
    X = type(C.__name__, (C, IClass), {})
    return X # y regresamos de nuevo esa clase pero con una "herencia inyectada"


##############################################################
@agregar_interface # la funci�n de arriba aplicada a manera de decorador
class A(object):
    d = 0 # tambi�n as� se pueden agregar atributos

##############################################################
# no existe un m�todo main pero este truco es �til
# es mas, no es necesario el main
if __name__ == '__main__': # si quieren quitar este if dedenten las l�neas posteriores
    print A
    a= A()
    print a.d, a.x
    a.z = 777 # y tambi�n se puede agregar atributos y m�todos al vuelo
    print a.z
