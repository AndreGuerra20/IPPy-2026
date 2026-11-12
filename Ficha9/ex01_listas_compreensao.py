# Ficha 9 - Ex 1
# Dado o número natural n, construa a lista por compreensão.


# a) com todos os números ímpares até n
def criar_lista_a(n):
    return [i for i in range(1, n + 1) if i % 2 == 1]


# b) com todos os n números múltiplos de 6
#    (os n primeiros múltiplos, tal como na Ficha 8 Ex 1 a);
#     os múltiplos de 6 até n seriam [i for i in range(1, n + 1) if i % 6 == 0])
def criar_lista_b(n):
    return [6 * i for i in range(1, n + 1)]


# c) com todos os n cubos dos números n
def criar_lista_c(n):
    return [i ** 3 for i in range(1, n + 1)]


# d) com os n elementos da sucessão u(n) = n + (-1)^n
def criar_lista_d(n):
    return [i + (-1) ** i for i in range(1, n + 1)]


# e) com os n elementos da sucessão v(n) = n^n
def criar_lista_e(n):
    return [i ** i for i in range(1, n + 1)]


# f) com todos os números até n que terminam em 4 ou em 7
def criar_lista_f(n):
    return [i for i in range(1, n + 1) if i % 10 in (4, 7)]


# g) com todos os números até n que são múltiplos de 3 e de 5
def criar_lista_g(n):
    return [i for i in range(1, n + 1) if i % 3 == 0 and i % 5 == 0]


n = int(input('n = '))
print('a)', criar_lista_a(n))
print('b)', criar_lista_b(n))
print('c)', criar_lista_c(n))
print('d)', criar_lista_d(n))
print('e)', criar_lista_e(n))
print('f)', criar_lista_f(n))
print('g)', criar_lista_g(n))
