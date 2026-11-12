# Ficha 6 - Ex 2
# Função que, dado um ângulo positivo x (em graus), devolve o valor aproximado do seno
# (fórmula de Bhaskara):  sin(x) ~ 4x(180 - x) / (40500 - x(180 - x))
# A fórmula é válida em [0, 180]; para ]180, 360[ usa-se sin(x) = -sin(x - 180).
import math


def seno_aproximado(x):
    """Devolve o seno aproximado do ângulo x (graus)."""
    x = x % 360
    sinal = 1
    if x > 180:
        x = x - 180
        sinal = -1
    return sinal * 4 * x * (180 - x) / (40500 - x * (180 - x))


angulo = float(input('Ângulo (graus): '))
print('Seno aproximado:', seno_aproximado(angulo))
print('math.sin:       ', math.sin(math.radians(angulo)))
