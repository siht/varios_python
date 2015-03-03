#! c:\python27\python.exe
# autor Jose Carlos Tzompantzi de Jesus
# fecha de inicio 17-09-2013 8:45
# pruebas del algoritmo de cifrado DES
# generado en base a teoria
# este codigo no es una implementacion optimizada al 100%,
# mas bien trata de seguir los pasos al pie de la letra.
# licenciado bajo copy-left o licencia GNU-GPL

perm0 = (\
57, 49, 41, 33, 25, 17,  9, 1,\
59, 51, 43, 35, 27, 19, 11, 3,\
61, 53, 45, 37, 29, 21, 13, 5,\
63, 55, 47, 39, 31, 23, 15, 7,\
56, 48, 40, 32, 24, 16,  8, 0,\
58, 50, 42, 34, 26, 18, 10, 2,\
60, 52, 44, 36, 28, 20, 12, 4,\
62, 54, 46, 38, 30, 22, 14, 6 \
)

expan0 = (\
(31,  4),\
( 3,  8),\
( 7, 12),\
(11, 16),\
(15, 20),\
(19, 24),\
(23, 28),\
(27,  0) \
)

perm1 = (\
56, 48, 40, 32, 24, 16,  8,  7,\
 0, 57, 49, 41, 33, 25, 17, 15,\
 9,  1, 58, 50, 42, 34, 26, 23,\
18, 10,  2, 59, 51, 43, 35, 31,\
62, 54, 46, 38, 30, 22, 14, 39,\
 6, 61, 53, 45, 37, 29, 21, 47,\
13,  5, 60, 52, 44, 36, 28, 55,\
20, 12,  4, 27, 19, 11,  3, 63 \
)

comp0 = (\
14, 18, 11, 26,  0,  4,  9,  7,\
 2, 30, 16,  5, 22, 10, 19, 15,\
25, 20, 12,  3, 28,  8, 24, 23,\
17,  6, 29, 21, 13,  1, 27, 31,\
45, 58, 34, 41, 52, 61, 38, 39,\
33, 44, 57, 50, 36, 53, 42, 47,\
49, 54, 43, 62, 37, 59, 48, 55,\
51, 46, 56, 40, 32, 35, 60, 63 \
)


corrimientos = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

s1 = (\
14,  4, 13, 1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9, 0,  7,\
 0, 15,  7, 4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5, 3,  8,\
 4,  1, 14, 8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10, 5,  0,\
15, 12,  8, 2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0, 6, 13 \
)

s2 = (\
15,  1,  8, 14,  6, 11,  3,  4,  9, 7,  2, 13, 12, 0,  5, 10,\
 3, 13,  4,  7, 15,  2,  8, 14, 12, 0,  1, 10,  6, 9, 11,  5,\
 0, 14,  7, 11, 10,  4, 13,  1,  5, 8, 12,  6,  9, 3,  2, 15,\
13,  8, 10,  1,  3, 15,  4,  2, 11, 6,  7, 12,  0, 5, 14,  9 \
)

s3 = (\
10,  0,  9, 14, 6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,\
13,  7,  0,  9, 3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,\
13,  6,  4,  9, 8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,\
 1, 10, 13,  0, 6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 \
)

s4=(\
 7, 13, 14, 3,  0,  6,  9, 10,  1, 2, 8,  5, 11, 12,  4, 15,\
13,  8, 11, 5,  6, 15,  0,  3,  4, 7, 2, 12,  1, 10, 14,  9,\
10,  6,  9, 0, 12, 11,  7, 13, 15, 1, 3, 14,  5,  2,  8,  4,\
 3, 15,  0, 6, 10,  1, 13,  8,  9, 4, 5, 11, 12,  7,  2, 14 \
)

s5=(\
 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13, 0, 14,  9,\
14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3, 9,  8,  6,\
 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6, 3,  0, 14,\
11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10, 4,  5,  3 \
)

s6=(\
12,  1, 10, 15, 9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,\
10, 15,  4,  2, 7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,\
 9, 14, 15,  5, 2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,\
 4,  3,  2, 12, 9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13 \
)

s7=(\
 4, 11,  2, 14, 15, 0,  8, 13,  3, 12, 9,  7,  5, 10, 6,  1,\
13,  0, 11,  7,  4, 9,  1, 10, 14,  3, 5, 12,  2, 15, 8,  6,\
 1,  4, 11, 13, 12, 3,  7, 14, 10, 15, 6,  8,  0,  5, 9,  2,\
 6, 11, 13,  8,  1, 4, 10,  7,  9,  5, 0, 15, 14,  2, 3, 12 \
)

s8=(\
13,  2,  8, 4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,\
 1, 15, 13, 8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,\
 7, 11,  4, 1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,\
 2,  1, 14, 7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11 \
)

perm_p = (\
27, 10, 35, 40,  4,  5,  6,  7,\
56, 19, 51, 32, 12, 13, 14, 15,\
 0, 26, 42, 49, 20, 21, 22, 23,\
 8, 33, 58, 17, 28, 29, 30, 31,\
 1, 11, 43, 25, 36, 37, 38, 39,\
59, 50,  2, 16, 44, 45, 46, 47,\
34, 24, 57,  9, 52, 53, 54, 55,\
41, 18,  3, 48, 60, 61, 62, 63 \
)

perm_f = (\
39, 7, 47, 15, 55, 23, 63, 31,\
38, 6, 46, 14, 54, 22, 62, 30,\
37, 5, 45, 13, 53, 21, 61, 29,\
36, 4, 44, 12, 55, 20, 60, 28,\
35, 3, 43, 11, 51, 19, 59, 27,\
34, 2, 42, 10, 50, 18, 58, 26,\
33, 1, 41,  9, 49, 17, 57, 25,\
32, 0, 40,  8, 48, 16, 56, 24 \
)


def showbits(arr, bitlen = 8):
    return '\n'.join(((e and bitlen or bitlen-1) - e.bit_length())*'0'+bin(e)[2:] for e in arr)

def permutar(arr, orden = []):
    '''permuta solo tablas de 8 elementos suponiendo que los numeros dados
    tienen 8 bits cada uno'''
    contador = 0; salida = [0,0,0,0,0,0,0,0]
    for elemento in orden:
        salida[contador >> 3] |= 1 << (7-(contador & 7)) if arr[elemento >> 3] & (1 << (7-(elemento & 7))) else 0
        contador +=1
    return salida

def divide(arr):
    '''regresa una tabla con dos elementos del mismo tamano'''
    return arr[:len(arr)>>1], arr[len(arr)>>1:]

def expander(arr, orden = []):
    '''expande una tabla de cuatro elementos con un 8 bits
    y la deja logicamente en una tabla de 8 elementos de 4 bits
    dividiendo cada 8 bits en cuatro, y agregando dos bits uno al principio
    y otro al final los cuales estan definidos en una tabla de 8 con tuplas
    de dos numero que indican el bit a repetir'''
    arr2 = []; contador = 0; vals = []
    for i in arr:
        arr2.append(i >> 4)
        arr2.append(i & 0xf)
    for elemento in orden:
        aux0 = arr2[elemento[0] >> 2] & (1 << (3 - elemento[0] % 4))
        aux1 = arr2[elemento[1] >> 2] & (1 << (3 - elemento[1] % 4))
        vals.append((aux0,aux1))
        contador += 1
    contador = 0
    for e in vals:
        arr2[contador] <<= 1
        arr2[contador] |= (0b100000 if e[0] else 0) | (1 if e[1] else 0)
        contador += 1
    return arr2

def despLS(arr, des):
    val = (arr[0] & (((1 << des) - 1) << (7 - des))) >> (7-des)
    bits = 0; sal = []
    for i in arr:
        bits |= i
        bits <<= 7
    bits >>= 7
    bits = (bits << des) | val
    while len(sal)<4:
        sal.insert(0,int(bits & 127))
        bits >>= 7
    return sal

def compactar(arr):
    s = [i << 1 for i in arr]
    s = permutar(s, comp0)
    return [i >> 2 for i in s]

def selector(num):
    return ((num & 1)|(0b10 if num & 0b100000 else 0),(num >>1) & 0b1111)

def foooooooo(l,r,k):
    d0xor = [r[i]^k[i] for i in range(len(r))]
    coord = [selector(i) for i in d0xor]
    sal = []
    fs = (s1,s2,s3,s4,s5,s6,s7,s8)
    for i in range(len(fs)):
        sal.append(fs[i][(coord[i][0]<<4) + coord[i][1]])
    sal = [i << 4 for i in sal]
    sal = permutar(sal, perm_p)
    sal = [i >> 4 for i in sal]
    l0 = []
    for i in l:
        l0.append(i>>4)
        l0.append(i&0xf)
    rnplus = [sal[i]^l0[i] for i in range(len(sal))]
    return [(rnplus[i]<<4) | rnplus[i+1] for i in range(0,len(rnplus),2)]

def defoo(cyph,k):
    l,r = cyph[:len(cyph)>>1], cyph[len(cyph)>>1:]
    r0 = expander(r, expan0)
    xor = [k[i] ^ r0[i] for i in range(len(k))]
    coord = [selector(i) for i in xor]
    fs = (s1,s2,s3,s4,s5,s6,s7,s8)
    sal = []
    for i in range(len(fs)):
        sal.append(fs[i][(coord[i][0]<<4) + coord[i][1]])
    pp = permutar(sal, perm_p)
    ll = []
    for i in l:
        ll.append(i>>4)
        ll.append(i&0xf)
    xorll = [pp[i] ^ ll[i] for i in range(len(ll))]
    return r+[(xorll[i]<<4) | xorll[i+1] for i in range(0,len(xorll),2)]

def main():
    #inicio de base des
    m = bytearray('unydad 2')
##    m = bytearray([i<<4 | i+1 for i in range(0,16,2)])
    print 'mensaje',m
    pi = permutar(m, perm0)
    l,r = divide(pi)
    r0 = expander(r,expan0)
    #fin de base des
    # inicio de generacion de llaves
    k = bytearray('Santiago')
##    k = [1,3,3,4,5,7,7,9,9,0xb,0xb,0xc,0xd,0xf,0xf,1]
##    k = bytearray([k[i]<<4 | k[i+1] for i in range(0,16,2)])
    k = [i << 1 for i in k]
    kplus = permutar(k, perm1)
    kplus = [i >> 1 for i in kplus]
    c0,d0 = divide(kplus)
##    print c0, d0
    cd1_16 = [despLS(c0, corrimientos[0])+ despLS(d0, corrimientos[0])]
    cont = 0
    while cont < len(corrimientos) - 1:
        cd1_16.append(despLS(cd1_16[cont][:4], corrimientos[cont +1] ) + despLS(cd1_16[cont][4:], corrimientos[cont +1] ))
        cont += 1
    subk1_16 = [compactar(i) for i in cd1_16]
    ### fin de generacion de llaves
    ## inicio de cifrado
    perfoo = [(r,foooooooo(l, r0, subk1_16[0]))]
    for i in range(1,len(subk1_16)):
        perfoo.append((perfoo[i-1][1],foooooooo(perfoo[i-1][0],expander(perfoo[i-1][1], expan0),subk1_16[i])))
    print showbits(perfoo[-1][0])
    print showbits(perfoo[-1][1])
    cypher = bytearray(permutar(perfoo[-1][1]+perfoo[-1][0], perm_f))
    print 'cifrado',cypher
##    print showbits(cypher)
    ##############################
    ## paso de descifrado
    nm = cypher
    npi = permutar(nm, perm0)
    nl,nr = divide(npi)
    nr0 = expander(nr,expan0)
    subk16_1 = subk1_16[:]
    subk16_1.reverse()
    desfoo = [(nr, foooooooo(nl,nr0,subk16_1[0]))]
    for i in range(1,len(subk16_1)):
        desfoo.append((desfoo[i-1][1],foooooooo(desfoo[i-1][0],expander(desfoo[i-1][1],expan0),subk16_1[i])))
    decode = bytearray(permutar(desfoo[15][1]+desfoo[15][0], perm_f))
    print 'descifrado',decode
    
if __name__ == '__main__':
    main()
