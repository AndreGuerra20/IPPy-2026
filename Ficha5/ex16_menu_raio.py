# Ficha 5 - Ex 16
# Dado o raio, apresente um menu que permita calcular a área e o perímetro da
# circunferência (A) ou a área e o volume da esfera (B), com duas casas decimais.
import math

raio = float(input('Raio: '))
while raio <= 0:
    print('O raio tem de ser maior do que zero!')
    raio = float(input('Raio: '))

opcao = ''
while opcao != 'S':
    print('A - Área e perímetro da circunferência')
    print('B - Área e volume da esfera')
    print('S - Sair')
    opcao = input('Opção: ').upper()
    if opcao == 'A':
        print(f'Área: {math.pi * raio ** 2:.2f}')
        print(f'Perímetro: {2 * math.pi * raio:.2f}')
    elif opcao == 'B':
        print(f'Área: {4 * math.pi * raio ** 2:.2f}')
        print(f'Volume: {4 / 3 * math.pi * raio ** 3:.2f}')
    elif opcao != 'S':
        print('Opção inválida')
