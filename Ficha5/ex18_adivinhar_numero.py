# Ficha 5 - Ex 18
# O utilizador tem 5 tentativas para adivinhar um número aleatório entre 1 e 15.
# Em cada tentativa é informado se o número é maior ou menor.
# (Versão sem break, que não é permitido na UC: o ciclo pára pela condição.)
import random as rd

numero = rd.randint(1, 15)

tentativa = 0
acertou = False
while tentativa < 5 and not acertou:
    tentativa += 1
    numero_adivinhado = int(input(f"Tentativa {tentativa}/5 - insira um número inteiro: "))
    if numero_adivinhado == numero:
        acertou = True
    elif numero_adivinhado < numero:
        print("O número é maior")
    else:
        print("O número é menor")

if acertou:
    print("Acertou em", tentativa, "tentativa(s)!")
else:
    print("Perdeu, esgotou o número de tentativas. O número era", numero)
