# Ficha 6 - Ex 3
# Função que, dada a distância D (m) e as velocidades v1 e v2 (m/s) de dois objetos que
# se deslocam um em direção ao outro, devolve o tempo que demoram a encontrar-se,
# em hora-minuto-segundo.


def tempo_encontro(distancia, v1, v2):
    """Devolve (horas, minutos, segundos) até os dois objetos se encontrarem."""
    t = distancia / (v1 + v2)          # as velocidades somam-se (sentidos opostos)
    horas = int(t // 3600)
    minutos = int(t % 3600 // 60)
    segundos = t % 60
    return horas, minutos, segundos


d = float(input('Distância (m): '))
vel1 = float(input('Velocidade do objeto 1 (m/s): '))
vel2 = float(input('Velocidade do objeto 2 (m/s): '))

if vel1 + vel2 > 0:
    h, m, s = tempo_encontro(d, vel1, vel2)
    print(f'Encontram-se ao fim de {h}h {m}min {s:.2f}s')
else:
    print('Os objetos nunca se encontram!')
