# Ficha 8 - Ex 1
# Dado o número natural n, construa o tuplo por compreensão.


# a) com todos os n números múltiplos de 3
def criar_tuplo_a(n):
    t = tuple(3 * i for i in range(1, n + 1))
    return t


# b) com todos os n pares da forma (n, n²)
#    (versão original: só os i pares -> tuple((i, i**2) for i in range(1, n+1) if i % 2 == 0))
def criar_tuplo_b(n):
    t = tuple((i, i ** 2) for i in range(1, n + 1))
    return t


# c) com todos os n ternos da forma (n, n³, n³ - n²)
def criar_tuplo_c(n):
    t = tuple((i, i ** 3, i ** 3 - i ** 2) for i in range(1, n + 1))
    return t


# d) com todos os números até n que são múltiplos de 4 e de 6
def criar_tuplo_d(n):
    t = tuple(i for i in range(1, n + 1) if i % 4 == 0 and i % 6 == 0)
    return t


# e) com todos os números até n que são ímpares e terminam em 5
def criar_tuplo_e(n):
    t = tuple(i for i in range(1, n + 1) if i % 2 == 1 and i % 10 == 5)
    return t


n = int(input('n = '))
print('a)', criar_tuplo_a(n))
print('b)', criar_tuplo_b(n))
print('c)', criar_tuplo_c(n))
print('d)', criar_tuplo_d(n))
print('e)', criar_tuplo_e(n))
