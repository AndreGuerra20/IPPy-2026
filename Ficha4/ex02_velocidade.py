# Ficha 4 - Ex 2
# Dada a distância D (m) percorrida em movimento retilíneo uniforme no tempo t (s),
# determine a velocidade v (m/s).

distancia = float(input('Distância (m): '))
tempo = float(input('Tempo (s): '))

if tempo <= 0:
    print('O tempo tem de ser maior do que zero!')

if tempo > 0:
    velocidade = distancia / tempo
    print(f'Velocidade: {velocidade:.2f} m/s')
