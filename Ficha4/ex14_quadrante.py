# Ficha 4 - Ex 14
# Dado o valor de um ângulo (em graus), no sentido positivo, determine o quadrante.

angle = 271
angle = angle % 360        # ângulos maiores do que 360 voltam ao intervalo [0, 360[

if 0 < angle < 90:
    print("Primeiro Quadrante")
elif 90 < angle < 180:
    print("Segundo Quadrante")
elif 180 < angle < 270:
    print("Terceiro Quadrante")
elif 270 < angle < 360:
    print("Quarto Quadrante")
else:
    print("O ângulo está sobre um dos eixos")


# Ficha 4 Ex 14 Alternativo (com radianos)
import math as mt

angle_rad = mt.radians(angle)
if 0 < angle_rad < mt.pi / 2:
    print("Primeiro Quadrante")
elif mt.pi / 2 < angle_rad < mt.pi:
    print("Segundo Quadrante")
elif mt.pi < angle_rad < 3 * mt.pi / 2:
    print("Terceiro Quadrante")
elif 3 * mt.pi / 2 < angle_rad < 2 * mt.pi:
    print("Quarto Quadrante")
else:
    print("O ângulo está sobre um dos eixos")
