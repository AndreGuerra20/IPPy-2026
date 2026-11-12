# Ficha 5 - Ex 15
# Enquanto o utilizador não digitar um valor negativo, vá pedindo um ângulo e indicando o
# quadrante a que pertence.

angulo = float(input('Ângulo (negativo para terminar): '))
while angulo >= 0:
    resto = angulo % 360
    if 0 < resto < 90:
        print('Primeiro quadrante')
    elif 90 < resto < 180:
        print('Segundo quadrante')
    elif 180 < resto < 270:
        print('Terceiro quadrante')
    elif 270 < resto < 360:
        print('Quarto quadrante')
    else:
        print('Está sobre um dos eixos')
    angulo = float(input('Ângulo (negativo para terminar): '))
