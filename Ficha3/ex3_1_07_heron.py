# Ficha 3 - 3.1 Ex 7
# Dados os três lados de um triângulo, determine a área usando a fórmula de Héron.
import math

a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))

p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print('Área:', area)
