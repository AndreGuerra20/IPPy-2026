# Ficha 5 - Ex 19
# O jogador começa com 15 € de saldo. Em cada jogada adivinha cara (0) ou coroa (1):
# se acerta ganha 2 €, se erra perde 3 €. O jogo termina sem saldo ou ao chegar a 20 €.
import random

saldo = 15
while 0 < saldo < 20:
    print('Saldo atual:', saldo, '€')
    aposta = input('Cara (0) ou coroa (1)? ')
    while aposta not in ('0', '1'):
        aposta = input('Opção inválida. Cara (0) ou coroa (1)? ')

    moeda = random.randint(0, 1)
    if moeda == 0:
        print('Saiu cara')
    else:
        print('Saiu coroa')

    if int(aposta) == moeda:
        saldo += 2
        print('Acertou! +2 €')
    else:
        saldo -= 3
        print('Errou! -3 €')

if saldo >= 20:
    print('Parabéns, ganhou! Saldo final:', saldo, '€')
else:
    print('Ficou sem saldo. Saldo final:', saldo, '€')
