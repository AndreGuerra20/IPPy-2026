# Ficha 3 - 3.1 Ex 10
# Dada a velocidade inicial v0, o ângulo de saída (em graus) e um instante t,
# determine a altura h e a velocidade instantânea v do projétil nesse instante.
import math

G = 9.8

v0 = float(input('Velocidade inicial (m/s): '))
angulo = float(input('Ângulo de saída (graus): '))
t = float(input('Instante t (s): '))

theta = math.radians(angulo)
h = v0 * t * math.sin(theta) - 0.5 * G * t ** 2
v = math.sqrt(v0 ** 2 - 2 * v0 * G * t * math.sin(theta) + G ** 2 * t ** 2)

print('Altura (m):', h)
print('Velocidade (m/s):', v)
