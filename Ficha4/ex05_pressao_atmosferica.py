# Ficha 4 - Ex 5
# Dada a altura h (h > 0), determine o valor aproximado (inteiro) da pressão atmosférica
# p(h) = p0 * e^(-h / h0), com p0 = 100 kPa e h0 = 8400 m.
import math

P0 = 100      # kPa
H0 = 8400     # m

altura = float(input('Altura acima do nível do mar (m): '))

if altura <= 0:
    print('A altura tem de ser maior do que zero!')

if altura > 0:
    pressao = P0 * math.exp(-altura / H0)
    print('Pressão atmosférica:', round(pressao), 'kPa')
