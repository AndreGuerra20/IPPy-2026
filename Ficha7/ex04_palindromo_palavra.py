# Ficha 7 - Ex 4
# Dada uma palavra, verifique se é um palíndromo.


def e_palindromo(palavra):
    """Compara as letras das pontas para o meio."""
    palavra = palavra.lower()            # Passar para minúsculas
    palavra = palavra.replace(" ", "")   # Remover espaços
    inicio = 0
    fim = len(palavra) - 1
    iguais = True
    while inicio < fim and iguais:
        if palavra[inicio] != palavra[fim]:
            iguais = False
        inicio += 1
        fim -= 1
    return iguais


def e_palindromo_alternativo(palavra):
    """Compara a palavra com a palavra invertida."""
    palavra = palavra.lower()            # Passar para minúsculas
    palavra = palavra.replace(" ", "")   # Remover espaços
    return palavra == palavra[::-1]


for p in ('ama', 'ovo', 'radar', 'reviver', 'salas', 'python'):
    print(p, e_palindromo(p), e_palindromo_alternativo(p))

texto = input('Palavra: ')
if e_palindromo(texto):
    print(texto, 'é um palíndromo')
else:
    print(texto, 'não é um palíndromo')
