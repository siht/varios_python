# -*- coding: cp1252 -*-
PERMITIDOS = 'WTYUIOAHXVM08mnvxñloiuytw '
print 'el espejo'
cadena = raw_input('introduce una texto\n')
reversa = cadena[::-1]
regla = lambda c: c if c in PERMITIDOS else '*'
generador = (regla(i) for i in reversa)
respuesta = ''.join(generador)
print respuesta
