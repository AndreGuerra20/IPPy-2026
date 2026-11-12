# Ficha 5 - Ex 17
# Enquanto o utilizador desejar continuar, apresente um menu com as opções dos
# exercícios 1 a 4 e execute o exercício escolhido.

opcao = ''
while opcao != '0':
    print()
    print('=== Menu ===')
    print('1 - Tabuada')
    print('2 - Quociente e resto')
    print('3 - Números pares entre dois números')
    print('4 - Capicuas entre dois números')
    print('0 - Sair')
    opcao = input('Opção: ')

    if opcao == '1':
        numero = int(input('Número natural: '))
        for i in range(1, 11):
            print(f'{numero} x {i} = {numero * i}')

    elif opcao == '2':
        numero = int(input('Número natural: '))
        for divisor in range(2, numero):
            print(f'{numero} // {divisor} = {numero // divisor}   resto = {numero % divisor}')

    elif opcao == '3':
        numero1 = int(input('1.º número: '))
        numero2 = int(input('2.º número: '))
        if numero1 > numero2:
            aux = numero1
            numero1 = numero2
            numero2 = aux
        soma = 0
        for i in range(numero1 + 1, numero2):
            if i % 2 == 0:
                print(i)
                soma += i
        print('Soma:', soma)

    elif opcao == '4':
        numero1 = int(input('1.º número: '))
        numero2 = int(input('2.º número: '))
        if numero1 > numero2:
            aux = numero1
            numero1 = numero2
            numero2 = aux
        for i in range(numero1, numero2 + 1):
            if str(i) == str(i)[::-1]:
                print(i)

    elif opcao != '0':
        print('Opção inválida')

print('Adeus!')
