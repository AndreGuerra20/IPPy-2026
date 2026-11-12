# Ficha 3 - 3.3 Ex 5
# Resolva o exercício anterior para frases (ignorando os espaços).

frase_a = 'ame o poema'
frase_b = 'a torre da derrota'
frase_c = 'roma me tem amor'

sem_espacos_a = frase_a.lower().replace(' ', '')
sem_espacos_b = frase_b.lower().replace(' ', '')
sem_espacos_c = frase_c.lower().replace(' ', '')

print('(a)', frase_a, '->', sem_espacos_a == sem_espacos_a[::-1])
print('(b)', frase_b, '->', sem_espacos_b == sem_espacos_b[::-1])
print('(c)', frase_c, '->', sem_espacos_c == sem_espacos_c[::-1])

frase = input('Escreva uma frase: ')
sem_espacos = frase.lower().replace(' ', '')
print('É palíndromo?', sem_espacos == sem_espacos[::-1])
