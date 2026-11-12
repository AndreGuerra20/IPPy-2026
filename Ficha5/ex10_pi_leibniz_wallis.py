# Ficha 5 - Ex 10
# Dado um número natural n, apresente a aproximação de pi usando n termos da fórmula de
# Leibniz e da fórmula de Wallis.
import math

n = int(input('Número de termos: '))

# Leibniz: pi/4 = soma de k=0 até infinito de (-1)^k / (2k + 1)
soma = 0
for k in range(n):
    soma += (-1) ** k / (2 * k + 1)
pi_leibniz = 4 * soma

# Wallis: pi/2 = produto de k=1 até infinito de 4k² / (4k² - 1)
produto = 1
for k in range(1, n + 1):
    produto *= 4 * k ** 2 / (4 * k ** 2 - 1)
pi_wallis = 2 * produto

print('Leibniz:', pi_leibniz, '  erro:', abs(math.pi - pi_leibniz))
print('Wallis: ', pi_wallis, '  erro:', abs(math.pi - pi_wallis))
print('math.pi:', math.pi)
