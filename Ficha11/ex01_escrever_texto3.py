# Ficha 11 - Ex 1
# Escrever o texto 'tres linhas\nem apenas\num ficheiro' no ficheiro texto3.txt.
# (O ficheiro é criado na pasta de trabalho atual.)

texto = 'tres linhas\nem apenas\num ficheiro'

# Versão com open / close
ficheiro = open('texto3.txt', 'w', encoding='utf-8')
ficheiro.write(texto)
ficheiro.close()

# Versão com a instrução with (o ficheiro é fechado automaticamente)
#with open('texto3.txt', 'w', encoding='utf-8') as ficheiro:
#    ficheiro.write(texto)

print('Ficheiro texto3.txt criado.')
