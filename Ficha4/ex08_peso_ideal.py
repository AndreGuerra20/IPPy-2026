# Ficha 4 - Ex 8
# Dados o género ('M' ou 'F') e a altura (m), determine o peso ideal:
# pM(h) = 72.7 * h - 58.0   e   pF(h) = 62.1 * h - 44.7

genero = input('Género (M/F): ').upper()
altura = float(input('Altura (m): '))

if genero == 'M':
    peso = 72.7 * altura - 58.0
    print(f'Peso ideal: {peso:.1f} kg')
else:
    if genero == 'F':
        peso = 62.1 * altura - 44.7
        print(f'Peso ideal: {peso:.1f} kg')
    else:
        print('Género inválido!')
