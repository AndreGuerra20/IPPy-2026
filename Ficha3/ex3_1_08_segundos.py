# Ficha 3 - 3.1 Ex 8
# Dados as horas, os minutos e os segundos, determine o número de segundos correspondentes.

horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total = horas * 3600 + minutos * 60 + segundos

print('Total de segundos:', total)
