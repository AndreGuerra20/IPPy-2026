# Ficha 5 - Ex 4
# Dados dois números naturais, apresente todas as capicuas que existem entre eles.

numero1 = int(input('1.º número: '))
numero2 = int(input('2.º número: '))

if numero1 > numero2:           # garantir que numero1 é o menor
    aux = numero1
    numero1 = numero2
    numero2 = aux

for i in range(numero1, numero2 + 1):
    texto = str(i)
    if texto == texto[::-1]:
        print(i)
