# Ficha 9 - Ex 3
# Construa uma lista de inteiros positivos até que o utilizador indique um número não
# positivo. No final apresente a soma dos pares e a soma dos ímpares.

lista = []

num = int(input("Introduza um número inteiro positivo (número não positivo para terminar): "))
while num > 0:
    lista.append(num)
    num = int(input("Introduza um número inteiro positivo (número não positivo para terminar): "))

soma_pares = sum(x for x in lista if x % 2 == 0)
soma_impares = sum(x for x in lista if x % 2 != 0)

print("Lista:", lista)
print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)
