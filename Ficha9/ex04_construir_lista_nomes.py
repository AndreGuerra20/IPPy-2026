# Ficha 9 - Ex 6
# Construa uma lista de nomes até que o utilizador indique 
# um caracter do conjunto {".",":",";"?","!"}.

lista_nomes = []
nome = input("Introduza um nome (ou um caracter do conjunto {'.',':',';','?','!'} para terminar): ")

while nome not in {".", ":", ";", "?", "!"}:
    lista_nomes.append(nome)
    nome = input("Introduza um nome (ou um caracter do conjunto {'.',':',';','?','!'} para terminar): ")

print("Lista de nomes:", lista_nomes)

# a) Obtenha a lista ordenada por ordem decrescente.
lista_ordenada_decrescente = lista_nomes[:]
lista_ordenada_decrescente.sort(reverse=True)
print("Nomes em ordem alfabética decrescente:", lista_ordenada_decrescente)


# a) Obtenha a lista ordenada por ordem decrescente.  Alternativo
#print("Nomes em ordem alfabética decrescente:", sorted(lista_nomes, reverse=True))

# b) Obtenha a lista ordenada por ordem crescente do comprimento de cada nome
lista_ordenada_comprimento = lista_nomes[:]
lista_ordenada_comprimento.sort(key=len)
print("Nomes ordenados por comprimento:", lista_ordenada_comprimento)

# c) Obtenha a lista inserindo o nome “Ana” em todas as posições múltiplas de 3.
lista_com_ana = []
for i in range(len(lista_nomes)):
    if i % 3 == 0:
        lista_com_ana.append("Ana")
    else:
        lista_com_ana.append(lista_nomes[i])
print("Nomes com Ana inserido em posições múltiplas de 3:", lista_com_ana)

# d) Obtenha a lista substituindo todas as ocorrências do segundo nome pelo último nome.
lista_substituida = []
segundo_nome = lista_nomes[1] 
ultimo_nome = lista_nomes[-1]

for i in range(len(lista_nomes)):
    if lista_nomes[i] == segundo_nome:
        lista_substituida.append(ultimo_nome)
    else:
        lista_substituida.append(lista_nomes[i])
print("Nomes com o segundo nome substituído pelo último:", lista_substituida)

# e) Obtenha a lista eliminando todos os nomes repetidos.
lista_sem_repetidos = []
for nome in lista_nomes:
    if nome not in lista_sem_repetidos:
        lista_sem_repetidos.append(nome)
print("Nomes sem repetição:", lista_sem_repetidos)

#f) Obtenha a lista eliminando todos os nomes cujo comprimento seja inferior a 5.
lista_comprimento_maior_ou_igual_5 = [nome for nome in lista_nomes if len(nome) >= 5]
print("Nomes com comprimento maior ou igual a 5:", lista_comprimento_maior_ou_igual_5)

# g) Obtenha a lista eliminando todos os nomes que sejam superiores a “Luís”.
lista_menor_ou_igual_luis = [nome for nome in lista_nomes if nome <= "Luís"]
print("Nomes menores ou iguais a 'Luís':", lista_menor_ou_igual_luis)

# h) Obtenha as três seguintes listas: lista 1 com todos os nomes entre “A” e “H”; a lista 2
# com todos os nomes superiores a “H” e inferiores a “P” e a lista 3 com todos os nomes
# entre “P” e “Z”.

lista1 = []
lista2 = []
lista3 = []


for nome in lista_nomes:
    letra_inicial = nome[0].upper()  # Considera a primeira letra do nome em maiúscula
    if "A" <= letra_inicial <= "H":
        lista1.append(nome)
    elif "H" < letra_inicial < "P":
        lista2.append(nome)
    elif "P" <= letra_inicial <= "Z":
        lista3.append(nome)
        
print("Nomes entre 'A' e 'H':", lista1)
print("Nomes entre 'H' e 'P':", lista2)
print("Nomes entre 'P' e 'Z':", lista3)