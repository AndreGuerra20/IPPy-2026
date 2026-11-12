# Ficha 8 - Ex 4
# Construa um tuplo de palavras até que o utilizador indique o ponto final. Para cada
# palavra, indique a frequência (%) com que aparece cada uma das vogais:
# frequência = número de vezes que aparece / número total de vogais * 100


def construir_tuplo_palavras():
    # pedir palavras enquanto o utilizador não inserir .
    palavras = ()
    palavra = input("Insira uma palavra: ")
    while palavra != ".":
        palavras += (palavra,)
        palavra = input("Insira uma palavra: ")
    # Devolver um tuplo com todas as palavras
    return palavras


def calcular_frequencias_vogais(palavra):
    vogais = ("a", "e", "i", "o", "u")
    palavra = palavra.lower()
    frequencias = ()
    # Contar o número de vogais
    numero_vogais = 0
    for letra in palavra:
        if letra in vogais:
            numero_vogais += 1
    # Calcular a frequência para a, e, i, o, u
    for vogal in vogais:
        if numero_vogais > 0:          # evita a divisão por zero (palavra sem vogais)
            frequencias += (palavra.count(vogal) / numero_vogais * 100,)
        else:
            frequencias += (0.0,)
    return frequencias


def programa():
    palavras = construir_tuplo_palavras()
    for palavra in palavras:
        frequencias = calcular_frequencias_vogais(palavra)
        print(palavra, end=': ')
        for i in range(len(frequencias)):
            print(f"{'aeiou'[i]}={frequencias[i]:.1f}%", end='  ')
        print()


programa()
