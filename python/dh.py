def operacion(base, primo, secreto):
    return base**secreto%primo

def primos(ultimo):
    primes = [2]
    if ultimo == 2:
        return primes
    impares = xrange(3, ultimo, 2)
    is_prime = 1
    for i in impares:
        for j in primes[:len(primes)<<1]:
            if i%j == 0:
                is_prime = 0
		break
        if is_prime:
            primes.append(i)
        is_prime = 1
    return primes

print primos(9999)
primo = raw_input('escribe un numero primo: ')
base = raw_input('escribe una base: ')
secreto_a = raw_input('escribe un numero secreto menor que el primo: ')

code_A = operacion(int(base), int(primo), int(secreto_a))

# mandamos a B base, primo, code_a

datos_B = (base, primo, code_A)
secreto_b = raw_input('escribe un numero secreto menor que el primo: ')

code_b = operacion(int(datos_B[0]), int(datos_B[1]), int(secreto_b))

#regresamos a A el code_b

#obtenemos llaves para ambos

llave_a = operacion(code_b, int(primo), int(secreto_a))
llave_b = operacion(datos_B[2], int(primo), int(secreto_b))

print llave_b, llave_a


