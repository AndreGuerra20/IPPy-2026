# Ficha 4 - Ex 21
# Dado um ângulo e usando os pontos subcolaterais como limites, determine a orientação
# (pontos cardeais ou colaterais) da rosa dos ventos.
# N = 0º, E = 90º, S = 180º, W = 270º; os limites são 22.5º, 67.5º, 112.5º, ...

angulo = float(input('Ângulo (graus): '))
angulo = angulo % 360

if angulo < 22.5 or angulo >= 337.5:
    print('N - Norte')
elif angulo < 67.5:
    print('NE - Nordeste')
elif angulo < 112.5:
    print('E - Este')
elif angulo < 157.5:
    print('SE - Sudeste')
elif angulo < 202.5:
    print('S - Sul')
elif angulo < 247.5:
    print('SW - Sudoeste')
elif angulo < 292.5:
    print('W - Oeste')
else:
    print('NW - Noroeste')
