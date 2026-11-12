# Ficha 5 - Ex 9
# Dado n, apresente todos os ternos pitagóricos (x, y, z) com x² + y² = z²
# e x, y, z em {1, 2, ..., n}.
# Considera-se x < y para não repetir o mesmo terno trocado, ex: (3,4,5) e (4,3,5).

n = int(input('Número natural: '))

for x in range(1, n + 1):
    for y in range(x + 1, n + 1):
        for z in range(y + 1, n + 1):
            if x ** 2 + y ** 2 == z ** 2:
                print((x, y, z))
