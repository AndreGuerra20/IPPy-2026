# Ficha 4 - Ex 1
# Dado o raio, apresente a área e o perímetro da circunferência e a área e o volume
# da esfera, com apenas duas casas decimais.
import math

raio = float(input('Raio: '))

if raio <= 0:
    print('O raio tem de ser maior do que zero!')

if raio > 0:
    print(f'Área da circunferência: {math.pi * raio ** 2:.2f}')
    print(f'Perímetro da circunferência: {2 * math.pi * raio:.2f}')
    print(f'Área da esfera: {4 * math.pi * raio ** 2:.2f}')
    print(f'Volume da esfera: {4 / 3 * math.pi * raio ** 3:.2f}')
