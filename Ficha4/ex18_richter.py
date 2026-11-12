# Ficha 4 - Ex 18
# Dada a magnitude de um terramoto, determine a classificação segundo a escala de Richter.

magnitude = float(input('Magnitude: '))

if magnitude < 0:
    print('Magnitude inválida')
elif magnitude < 4.0:
    print('Pequeno')
elif magnitude < 5.0:
    print('Ligeiro')
elif magnitude < 6.0:
    print('Moderado')
elif magnitude < 10.0:
    print('Grande')
else:
    print('Extremo')
