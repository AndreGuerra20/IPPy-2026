# Ficha 6 - Ex 4
# Função que, dados dois raios, devolve a área e o perímetro da coroa circular.
import math


def coroa_circular(raio1, raio2):
    """Devolve (área, perímetro) da coroa circular definida pelos dois raios."""
    area = math.pi * abs(raio1 ** 2 - raio2 ** 2)
    perimetro = 2 * math.pi * (raio1 + raio2)
    return area, perimetro


r1 = float(input('Raio 1: '))
r2 = float(input('Raio 2: '))
area, perimetro = coroa_circular(r1, r2)
print(f'Área: {area:.2f}')
print(f'Perímetro: {perimetro:.2f}')
