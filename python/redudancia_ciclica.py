'''programa de prueba de redundancia ciclica'''
from __future__ import print_function
if __name__ == '__main__':
    def main():
        mensaje = '1010101'
        comprobador = '1010'
        int_m = int(mensaje, 2)
        int_c = int(comprobador, 2)
        int_m <<= int_c.bit_length() - 1
        while int_c > int_m:
            int_m ^= int_c << int_m.bit_length() - int_c.bit_length()
        print(int_m)
        print('{0:b}'.format(int_m))

    main()
