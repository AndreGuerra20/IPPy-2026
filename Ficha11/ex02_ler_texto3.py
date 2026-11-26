# Ficha 11 - Ex 2
# Ler o ficheiro texto3.txt (criado no Ex 1 - executar primeiro o ex01) de vários modos.

# a) Ler o texto todo de uma vez
with open('texto3.txt', 'r', encoding='utf-8') as ficheiro:
    conteudo = ficheiro.read()
    print('a)', conteudo)

# b) Ler os primeiros 9 caracteres
# 1 caracter = 1 byte, mas alguns caracteres (acentuados) ocupam mais do que 1 byte.
with open('texto3.txt', 'r', encoding='utf-8') as ficheiro:
    conteudo = ficheiro.read(9)
    print('b)', conteudo)

# c) Ler o ficheiro linha a linha
print('c)', end='')
with open('texto3.txt', 'r', encoding='utf-8') as ficheiro:
    linha = ficheiro.readline()
    while linha != '':
        print(linha)
        linha = ficheiro.readline()

# c) Alternativa: percorrer o ficheiro com um for
with open('texto3.txt', 'r', encoding='utf-8') as ficheiro:
    for linha in ficheiro:
        print(linha)

# d) Ler as linhas todas de uma só vez (lista de linhas)
with open('texto3.txt', 'r', encoding='utf-8') as ficheiro:
    print('d)', ficheiro.readlines())
