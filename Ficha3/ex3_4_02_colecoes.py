# Ficha 3 - 3.4 Ex 2
# Construa as seguintes coleções ordenadas homogéneas.
import math

# a) Os 20 primeiros números naturais
print('(a)', tuple(range(1, 21)))

# b) Todos os números ímpares entre 17 e 35
print('(b)', tuple(range(17, 36, 2)))

# c) Todos os múltiplos de 6 entre 36 e 60
print('(c)', tuple(range(36, 61, 6)))

# d) Todos os ângulos múltiplos de pi/4 entre -2pi e 2pi
print('(d)', tuple(k * math.pi / 4 for k in range(-8, 9)))

# e) Os 15 primeiros números pares entre -20 e 20
print('(e)', tuple(range(-20, 9, 2)))

# f) Todos os quadrados perfeitos entre 1 e 1000
print('(f)', tuple(i ** 2 for i in range(1, 32)))
