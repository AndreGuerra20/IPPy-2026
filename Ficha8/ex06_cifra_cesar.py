# Ficha 8 - Ex 6
# Cifra de César: codificação E(x) = (x + n) mod 26 e descodificação D(x) = (x - n) mod 26.
# O alfabeto é o tuplo das 26 letras minúsculas da tabela ASCII ('a' = 97, ..., 'z' = 122).
# Os caracteres que não são letras minúsculas (espaços, pontuação) ficam iguais.

LETRAS = tuple(chr(codigo) for codigo in range(97, 123))


def codificar(mensagem, n):
    resultado = ''
    for caracter in mensagem.lower():
        if caracter in LETRAS:
            x = LETRAS.index(caracter)
            resultado += LETRAS[(x + n) % 26]
        else:
            resultado += caracter
    return resultado


def descodificar(mensagem, n):
    resultado = ''
    for caracter in mensagem.lower():
        if caracter in LETRAS:
            x = LETRAS.index(caracter)
            resultado += LETRAS[(x - n) % 26]
        else:
            resultado += caracter
    return resultado


texto = input('Mensagem: ')
troca = int(input('Troca (n): '))
cifrado = codificar(texto, troca)
print('Codificada:   ', cifrado)
print('Descodificada:', descodificar(cifrado, troca))
