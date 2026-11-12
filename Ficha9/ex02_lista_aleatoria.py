# Ficha 9 - Ex 2
# Dado o número de elementos, construa uma lista de inteiros aleatórios entre 1 e 100.
from random import randint

n = int(input("Número de elementos: "))
lista = [randint(1, 100) for _ in range(n)]
print("Lista:", lista)

# a) Maior e menor elemento
maior = max(lista)
menor = min(lista)
print("Maior:", maior, "| Menor:", menor)

# b) Índices onde aparecem o maior e o menor (podem repetir-se)
ind_maior = [i for i in range(len(lista)) if lista[i] == maior]
ind_menor = [i for i in range(len(lista)) if lista[i] == menor]
print("Índices do maior:", ind_maior, "| Índices do menor:", ind_menor)

# c) Soma de todos os elementos
soma = sum(lista)
print("Soma:", soma)

# d) Lista ordenada por ordem crescente
ordenada = sorted(lista)
print("Ordenada:", ordenada)

# e) Múltiplos de 5 substituídos por 0
sem_mult5 = [0 if x % 5 == 0 else x for x in lista]
print("Múltiplos de 5 a 0:", sem_mult5)

# e) Alternativo
sem_mult5 = []
for x in lista:
    if x % 5 == 0:
        sem_mult5.append(0)
    else:
        sem_mult5.append(x)
print("Múltiplos de 5 a 0 (alternativo):", sem_mult5)

# f) Eliminar os valores superiores a 35 e inferiores a 60
filtrada = [x for x in lista if not (35 < x < 60)]
print("Sem valores entre 35 e 60:", filtrada)

# g) Eliminar os valores cujos índices são múltiplos de 4
sem_ind4 = [lista[i] for i in range(len(lista)) if i % 4 != 0]
print("Sem índices múltiplos de 4:", sem_ind4)
