# Ficha 5 - Ex 6
# Dada uma frase, apresente o número de vogais e o número de consoantes.

frase = "Ola mundo 12345"

vogais = "aeiouáàâãéêíóôõú"
num_vogais = 0
num_consoantes = 0

for letra in frase.lower():
    if letra.isalpha():          # ignora espaços, números e pontuação
        if letra in vogais:
            num_vogais += 1
        else:
            num_consoantes += 1

print("Número de vogais:", num_vogais)
print("Número de consoantes:", num_consoantes)
