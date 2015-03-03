#!/usr/bin/env python

def inu(cad):
    return ''.join('0'*(8-i.bit_length()) + '{:b}'.format(i) for i in bytearray(cad))

def inu2(cad):
    return ''.join('{}{:b}'.format('0'*(8-i.bit_length()),i) for i in bytearray(cad))

def main():
    cadena = 'trydes'
    print '\n'.join(('0'*(8-i.bit_length())) + bin(i)[2:] for i in bytearray(cadena))
    print inu2(cadena)

if __name__ == '__main__':
    main()
