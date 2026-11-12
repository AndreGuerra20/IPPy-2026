# Ficha 5 - Ex 1
# Dado um número natural, apresente a tabuada desse número.

numero = int(input('Número natural: '))

# Com ciclo while
i = 1
while i <= 10:
    print(f'{numero} x {i} = {numero * i}')
    i += 1

print()

# Com ciclo for
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
