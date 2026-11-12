# Ficha 4 - Ex 3
# Dados o número de vitórias, empates e derrotas, determine os pontos de uma equipa.

vitorias = 20
empates = 10
derrotas = 4

pontos = vitorias * 3 + empates
print("A equipa fez: ", pontos, "pontos")


# Ficha 4 Ex 3 Alternativo
# Valida se o número de jogos é possível num campeonato a duas voltas com n_equipas
# (cada equipa joga 2 vezes com cada uma das outras: (n_equipas - 1) * 2 jogos).
n_equipas = 18
vitorias = 20
empates = 10
derrotas = 4

n_pontos = 0

if vitorias + empates + derrotas > (n_equipas - 1) * 2:
    print("Número de jogos impossível")
else:
    n_pontos = 3 * vitorias + 1 * empates
    print("A equipa fez: ", n_pontos, "pontos")
