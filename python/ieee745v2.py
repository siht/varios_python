# traduce 'registros' de 32 o 64 bits de su valor en punto flotante
# a su representacion decimal.
# suponiendo que en memoria se tiene para un float
# memoria    valor
# 0x00100    0x40400000
# o para un double
# memoria    valor
# 0x00100    0x00000000; parte baja
# 0x00104    0x40080000; parte alta
# no esta optimizado el codigo y solo es mi percepcion de como se ejecuta
# el codigo (asi lo entendi, pues)
# es una forma de entender el estandar ieee 754 y puede haber mas de una
# interpretacion


def ieeed(numero):
    '''convierte un numero de 64 bits a su equivalente en coma flotante de doble presicion (big endian)'''
    signo = numero >> 63
    exponente = (numero >> 52) & 0x7ff
    mantisa = numero & 0xfffffffffffff
    if exponente == 0x7ff and mantisa:
        return 'NaN'
    if exponente == 0x7ff and not mantisa:
        if signo:
            return '-infinito'
        return 'infinito'
    if not mantisa and not exponente:
        if signo:
            return '-0.0'
        return '0.0'
    cont = 0
    aux = 0
    while cont < 52:
        if (mantisa >> cont) & 1:
            aux += 2**-(52-cont)
        cont += 1
    if exponente:
        aux += 1
    if exponente:
        sal = aux*(2**(exponente-1023))
    else:
        sal = aux*(2**-1022)
    if signo:
        sal *= -1
    return str(sal)

def ieeef(numero):
    '''convierte un numero de 32 bits a su equivalente en coma flotante de simple presicion'''
    signo = numero >> 31
    exponente = (numero >> 23) & 0xff
    mantisa = numero & 0x7fffff
    if exponente == 0xff and mantisa:
        return 'NaN'
    if exponente == 0xff and not mantisa:
        if signo:
            return '-infinito'
        return 'infinito'
    if not mantisa and not exponente:
        if signo:
            return '-0.0'
        return '0.0'
    cont = 0
    aux = 0
    while cont < 23:
        if (mantisa >> cont) & 1:
            aux += 2**-(23-cont)
        cont += 1
    if exponente:
        aux += 1
    if exponente:
        sal = aux*(2**(exponente-127))
    else:
        sal = aux*(2**-126)
    if signo:
        sal *= -1
    return str(sal)
if __name__ == '__main__':
    print ieeef(0x40400000) #3
    print ieeed(0x4008000000000000)#3
    print ieeef(0x805C0000) # -8.44886564...x10^-39
    print ieeed(0xB807000000000E65) # -8.44886564...x10^-39
    print ieeed(0x3ff0000000000000) # 1
    print ieeed(0x3ff0000000000001) # 1.xxxxxx
    print ieeef(0x3E400000)
    print ieeef(1082130432)
