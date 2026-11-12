# Ficha 5 - Ex 3
# Dados dois números naturais, apresente os números pares que existem entre eles e a
# soma desses números.

numero1 = 12
numero2 = 35
soma = 0
if numero1 < numero2:
    for i in range(numero1 + 1, numero2):
        if i % 2 == 0:
            print(i)
            soma += i
else:
    for i in range(numero2 + 1, numero1):
        if i % 2 == 0:
            print(i)
            soma += i
print('Soma:', soma)


# Ficha 5 Ex 3 Alternativo (escolhe primeiro o intervalo e depois percorre-o uma só vez)
numero1 = 12
numero2 = 35
soma = 0
if numero1 < numero2:
    numeros_a_considerar = range(numero1 + 1, numero2)
else:
    numeros_a_considerar = range(numero2 + 1, numero1)

for i in numeros_a_considerar:
    if i % 2 == 0:
        print(i)
        soma += i
print('Soma:', soma)
