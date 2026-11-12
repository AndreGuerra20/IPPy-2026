# Ficha 3 - 3.1 Ex 5
# Dado o raio de uma circunferência, determine e apresente a área (I) e o perímetro (II),
# assim como a área (III) e o volume (IV) da correspondente esfera.
import math

raio = float(input('Raio: '))

area_circ = math.pi * raio ** 2
perimetro_circ = 2 * math.pi * raio
area_esfera = 4 * math.pi * raio ** 2
volume_esfera = 4 / 3 * math.pi * raio ** 3

print('Área da circunferência:', area_circ)
print('Perímetro da circunferência:', perimetro_circ)
print('Área da esfera:', area_esfera)
print('Volume da esfera:', volume_esfera)
