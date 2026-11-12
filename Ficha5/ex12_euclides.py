# Ficha 5 - Ex 12
# Dados dois números naturais, apresente a tabela do algoritmo de Euclides no cálculo do
# máximo divisor comum (mdc).

a = int(input('1.º número: '))
b = int(input('2.º número: '))

print(f'{"a":>8} {"b":>8} {"resto":>8}')
while b != 0:
    resto = a % b
    print(f'{a:>8} {b:>8} {resto:>8}')
    a = b
    b = resto

print('mdc =', a)
