# Ficha 10 - Ex 3
# Dada uma frase, construa o dicionário com cada letra e o número de vezes que aparece.


def contar_letras(frase):
    contagem = {}
    for letra in frase.lower():
        if letra.isalpha():
            contagem[letra] = contagem.get(letra, 0) + 1
    return contagem


texto = input('Frase: ')
resultado = contar_letras(texto)
print(resultado)
for letra in sorted(resultado):
    print(f'{letra}: {resultado[letra]}')
