#-------------------------------------------------------------------------------
# Name:        calculadora
# Purpose:
#
# Author:      Carlos
#
# Created:     18/05/2012
# Copyright:   (Cleft) Carlos 2012
# Licence:     el codigo es licenciado con gnu/gpl
#              vea en google como obtener su copia
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import re
from __init__ import *

class Octeto(object):
    def __init__(self,valor =0):
        object.__init__(self)
        self.__huevo = 666
        if valor == self.__huevo:
            raise Exception,"Pull me into your perfect circle"
        elif valor not in range(lim_hosts):
            raise Exception,"no es un numero host valido"
        self.__valor = 0
        self.__valor = valor

    def set_valor(self, valor):
        '''establece el valor del este objeto (rango 0-255)'''
        if valor not in range(lim_hosts):
            raise Exception,"no es un numero host valido"
        self.__valor = valor

    def get_valor(self):
        '''(int)obtiene el valor del este objeto'''
        return self.__valor

    Valor = property(get_valor, set_valor,doc='''(int)devuelve o establece el valor del este objeto (rango 0-255)''')

    def __str__(self):
        '''(str)muestra la cadena con el valor de este objeto'''
        return "%i" %self.__valor

    def __and__(self, b):
        '''(int)realiza la operacion 'and' bit a bit de los dos objetos'''
        return self.__valor & b.Valor

    def __or__(self,b):
        '''(int)realiza la operacion 'or' bit a bit de los dos objetos'''
        return self.__valor | b.Valor

    def __gt__(self,b):
        '''(True/False) indica si el primer octeto es mayor'''
        return True if self.__valor > b.__valor else False

    def __lt__(self,b):
        '''(True/False) indica si el primer octeto es menor'''
        return True if self.__valor < b.__valor else False

class Cuatro_Octetos(object):
    def __init__(self,direccion):
        object.__init__(self)
        self.__direccion = []
        self.__validar_datos(direccion)

    def __validar_datos(self,direccion):
        '''verifica que tenga cuatro octetos o una cadena con el formato adecuado'''
        if type(direccion) == list or type(direccion) == str or type(direccion) == unicode:
            if type(direccion) == list:
                if len(direccion) != 4:
                    raise Exception,"no tiene los elementos necesarios"
                for v in direccion:
                    if type(v) != Octeto:
                        raise Exception,"no son de tipo octeto"
                    else:
                        self.__direccion.append(v)
            if type(direccion) == str:
                if re.match("^\d{1,3}(\.\d{1,3}){3}$",direccion):
                    for n in direccion.split("."):
                        self.__direccion.append(Octeto(int(n)))
        else:
            raise Exception,"no es de tipo adecuado"

    def __str__(self):
        '''(str) devuelve una cadena con el formato de direcion ip xxx.xxx.xxx.xxx'''
        return ".".join(["%i" % n.Valor for n in self.__direccion])

    def get_direccion(self):
        '''(list)regresa la direccion asociada a este objeto con cuatro objetos Octeto'''
        return self.__direccion

class Mascara_subred(Cuatro_Octetos,object):
    def __init__(self,direccion = '0.0.0.0'):
        object.__init__(self)
        Cuatro_Octetos.__init__(self,direccion)
        self.__validar_datos()

    def __validar_datos(self):
        '''verifica que los datos de la mascara tengan un formato adecuado'''
        for oc in self.get_direccion():
            if oc.Valor not in permitidos and oc.Valor != 0:
                raise Exception, "no son validos esos valores para una mascara de subred"
        for i in range(3):
            if self.get_direccion()[i] < self.get_direccion()[i+1]:
                raise Exception,"un octeto precedente debe ser mas grande que el octeto que le sucede"
        self.__set_tipo()

    def __set_tipo(self):
        '''establece el tipo de la mascara de subred mediante la direccion de este mismo objeto'''
        cont=0
        self.__clase = None
        for i in range(4):
            if self.get_direccion()[i].Valor == 255:
                cont+=1
        if cont == 1:
            self.__clase= "A"
        elif cont == 2:
            self.__clase = "B"
        elif cont == 3:
            self.__clase = "C"

    def __get_tipo(self):
        '''(str/None) devuelve el tipo de mascara de subred de este objeto'''
        return self.__clase

    Clase = property(__get_tipo, doc = '''(str/None) devuelve el tipo de mascara de subred de este objeto''')

    def get_mascara(self):
        '''(list) devuelve la mascara relacionada a este objeto'''
        return self.get_direccion()

    def set_mascara(self,direccion):
        '''(list/str) establece la direccion relacionada a este objeto'''
        self.__init__(direccion)

    Mascara = property(get_mascara,set_mascara,doc= '''(list/str) establece/devuelve la direccion relacionada a este objeto''')

    def __str__(self):
        '''(str) devuelve una cadena con el formato de direcion ip xxx.xxx.xxx.xxx o ""'''
        if not self.get_direccion()[0].Valor:
            return ""
        else:
            return ".".join(["%i" % n.Valor for n in self.get_direccion()])

class Dir_Ip(Cuatro_Octetos, object):
    def __init__(self, direccion):
        object.__init__(self)
        Cuatro_Octetos.__init__(self,direccion)
        if self.get_direccion()[0].Valor in primeros:
            raise Exception, "esos numeros no se permiten en el primer octeto"
        if self.get_direccion()[3].Valor in ultimos:
            raise Exception, "esos numeros no se permiten en el ultimo octeto"
        self.__set_Tipo(self.get_direccion()[0])

    def __set_Tipo(self,oc):
        if oc.Valor in range(128):
            self.__clase = 'A'
        if oc.Valor in range(128,192):
            self.__clase = 'B'
        if oc.Valor in range(192,224):
            self.__clase = 'C'
        if oc.Valor in range(224,240):
            self.__clase = 'D'
        if oc.Valor in range(240,256):
            self.__clase = 'E'

    def get_Tipo(self):
        return self.__clase

    Clase = property(get_Tipo)

class Red(object):
    def __init__(self,ip = "1.0.0.1",ms = None):
        object.__init__(self)
        self.__validar_ip(ip)
        self.__set_clase(ms)
        self.__set_numero_hosts_segmento()
        self.__set_numero_redes()
        self.__set_numero_subredes()

    def __set_clase(self,ms):
        if ms == None:
            if self.__ip.Clase == clases_ip[0]:
                self.__ms = Mascara_subred('255.0.0.0')
            elif self.__ip.Clase == clases_ip[1]:
                self.__ms = Mascara_subred('255.255.0.0')
            elif self.__ip.Clase == clases_ip[2]:
                self.__ms = Mascara_subred('255.255.255.0')
            elif self.__ip.Clase == clases_ip[3]:
                self.__ms = Mascara_subred()
            elif self.__ip.Clase == clases_ip[4]:
                self.__ms = Mascara_subred()
        else:
            self.set_mascara(ms)
        self.__generar_ids()

    def __validar_ip(self,ip):
        if type(ip) == str or type(ip) == unicode:
            self.__ip = Dir_Ip(ip)
        elif type(ip) == Dir_Ip:
            self.__ip = ip
        elif type(ip) == unicode:
            self.__ip = Dir_Ip(ip)
        else:
            raise Exception, "debe ser tipo Dir_Ip o str"

    def get_ip(self):
        return self.__ip

    def set_ip(self,ip):
        self.__validar_ip(ip)
        self.__generar_ids()
        self.__set_clase(self.__ms.get_direccion())

    Ip = property( get_ip, set_ip,doc = '''muestra o establece la ip de esta red''' )

    def get_mascara(self):
        return self.__ms

    def set_mascara(self, ms):
        self.__ms = Mascara_subred(ms)
        if self.__ip.Clase > self.__ms.Clase:
            raise Exception,"la clase de la mascara de no debe ser mas grande que la clase de subred"
        self.__generar_ids()
        self.__set_numero_hosts_segmento()
        self.__set_numero_subredes()

    Mascara = property(get_mascara, set_mascara , doc = '''muestra o establece la mascara de subred de esta red''')

    def __generar_ids(self):
        aux = []
        if self.__ip.Clase != clases_ip[3] and self.__ip.Clase != clases_ip[4]:
            for i in range(4):
                aux.append(Octeto(self.Ip.get_direccion()[i] & self.Mascara.get_direccion()[i]))
            self.__ids = Cuatro_Octetos(aux)
        else:
            self.__ids = None

    def get_ids(self):
        return self.__ids

    def __set_numero_hosts_segmento(self):
        hosts = None
        if self.__ms.Clase:
            masc = self.__ms.get_direccion()
            aux = clases_mascara.index(self.__ms.Clase) - len(masc) + 1
            hosts = 256 - masc[aux].Valor
            aux += 1
            while aux:
                hosts *= 256
                aux += 1
            hosts -= 2 if hosts > 0 else 0
        self.__hosts = hosts

    def get_hosts_red_segmento(self):
        return self.__hosts

    N_hosts_por_segmento = property(get_hosts_red_segmento,doc='''muestra el numero de hosts por segmento de la red''')

    def __set_numero_redes(self):
        if self.__ip.Clase == clases_ip[0]:
            self.__n_redes = 126
        elif self.__ip.Clase == clases_ip[1]:
            self.__n_redes = 16384
        elif self.__ip.Clase == clases_ip[2]:
            self.__n_redes = 2097152

    def get_numero_redes(self):
        return self.__n_redes

    N_redes = property(get_numero_redes,doc='''muestra el numero de redes en base a tu ip''')

    def __set_numero_subredes(self):
        subredes = None
        if self.__ms.Clase:
            masc = self.__ms.get_direccion()
            i = clases_mascara.index(self.__ms.Clase) +1
            if self.__ms.get_direccion()[i].Valor:
                desp = -(permitidos.index(masc[i].Valor) - len(permitidos) + 1)
                subredes = (masc[i].Valor >> desp) + 1
            else:
                subredes = 1
            i -= 1
            i -= clases_mascara.index(self.__ip.Clase)
            subredes *= 256**i
            if subredes == 1:
                subredes = None
        self.__subredes = subredes

    def get_subredes(self):
        return self.__subredes

    Subredes = property(get_subredes)

if __name__ == "__main__":
    try:
        red = Red("12.18.100.1","255.255.192.0")
    except Exception:
        print Exception
    print red
    print red.Ip
    print red.Mascara.get_direccion()
    print red.Mascara.Clase
    print red.Ip.Clase
    print red.get_ids()
    print red.N_hosts_por_segmento
    print red.Subredes
