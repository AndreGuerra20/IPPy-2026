# Ficha 5 - Ex 20
# Jogo "pedra-papel-tesoura" contra o computador, enquanto o utilizador desejar jogar.
# Regra extra: não é permitido mostrar "pedra" duas vezes seguidas.
# No final indica-se quem ganhou o jogo (mais jogadas ganhas).
import random

opcoes = ('pedra', 'papel', 'tesoura')

vitorias_jogador = 0
vitorias_computador = 0
empates = 0
anterior_jogador = ''
anterior_computador = ''

continuar = 's'
while continuar == 's':
    jogador = input('pedra, papel ou tesoura? ').lower()
    while jogador not in opcoes or (jogador == 'pedra' and anterior_jogador == 'pedra'):
        if jogador == 'pedra':
            print('Não pode jogar pedra duas vezes seguidas!')
        else:
            print('Opção inválida!')
        jogador = input('pedra, papel ou tesoura? ').lower()

    computador = opcoes[random.randint(0, 2)]
    while computador == 'pedra' and anterior_computador == 'pedra':
        computador = opcoes[random.randint(0, 2)]

    print('Computador jogou:', computador)

    if jogador == computador:
        print('Empate')
        empates += 1
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'tesoura' and computador == 'papel') or \
         (jogador == 'papel' and computador == 'pedra'):
        print('Ganhou esta jogada!')
        vitorias_jogador += 1
    else:
        print('Perdeu esta jogada!')
        vitorias_computador += 1

    anterior_jogador = jogador
    anterior_computador = computador
    continuar = input('Continuar a jogar (s/n)? ').lower()

print(f'Jogador {vitorias_jogador} - {vitorias_computador} Computador ({empates} empates)')
if vitorias_jogador > vitorias_computador:
    print('Ganhou o jogo!')
elif vitorias_jogador < vitorias_computador:
    print('O computador ganhou o jogo!')
else:
    print('O jogo terminou empatado!')
