# Ficha 7 - Ex 5
# Resolva o exercício anterior para frases (os espaços são ignorados).


def e_palindromo(frase):
    """Devolve True se a frase (sem espaços e em minúsculas) for um palíndromo."""
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]


frases = ('ame o poema', 'a torre da derrota', 'roma me tem amor', 'ola mundo')
for frase in frases:
    print(f"'{frase}' ->", e_palindromo(frase))
