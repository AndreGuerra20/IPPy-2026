# Ficha 3 - 3.1 Ex 6
# Dados os lados de um retângulo, determine e apresente a área, o perímetro,
# o comprimento das diagonais e o valor de um dos ângulos agudos (em graus).
import math

comprimento = float(input('Comprimento: '))
largura = float(input('Largura: '))

area = comprimento * largura
perimetro = 2 * (comprimento + largura)
diagonal = math.sqrt(comprimento ** 2 + largura ** 2)
# ângulo agudo entre a diagonal e o lado maior
angulo = math.degrees(math.atan(min(comprimento, largura) / max(comprimento, largura)))

print('Área:', area)
print('Perímetro:', perimetro)
print('Diagonal:', diagonal)
print('Ângulo agudo (graus):', angulo)
