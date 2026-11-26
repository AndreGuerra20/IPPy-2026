# Ficha 11 - Ex 4
# a) Guardar as notas num ficheiro .csv com os campos separados por ";"
# b) Verificar o conteúdo do ficheiro no Bloco de Notas  (manual)
# c) Verificar se o Excel abre o ficheiro corretamente    (manual: o Excel em
#    português usa ";" como separador, por isso abre as colunas corretamente)
# d) Ler a informação guardada no ficheiro csv
import csv

NOME_FICHEIRO = 'notas.csv'

notas = [['Nome', 'Teste 1', 'Teste 2', 'Teste 3'],
         ['Joaquim Silva', '10', '14', '12'],
         ['Maria Antonia', '11', '8', '18'],
         ['Jose Carlos', '14', '10', '10']]


# a) com o módulo csv
def guardar_csv(dados, nome_ficheiro):
    with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as ficheiro:
        escritor = csv.writer(ficheiro, delimiter=';')
        escritor.writerows(dados)


# a) alternativa sem o módulo csv
def guardar_csv_manual(dados, nome_ficheiro):
    with open(nome_ficheiro, 'w', encoding='utf-8') as ficheiro:
        for linha in dados:
            ficheiro.write(';'.join(linha) + '\n')


# d) com o módulo csv
def ler_csv(nome_ficheiro):
    dados = []
    with open(nome_ficheiro, 'r', newline='', encoding='utf-8') as ficheiro:
        leitor = csv.reader(ficheiro, delimiter=';')
        for linha in leitor:
            dados.append(linha)
    return dados


# d) alternativa sem o módulo csv
def ler_csv_manual(nome_ficheiro):
    dados = []
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        for linha in ficheiro:
            dados.append(linha.strip().split(';'))
    return dados


guardar_csv(notas, NOME_FICHEIRO)
print('Guardado em', NOME_FICHEIRO)
notas_lidas = ler_csv(NOME_FICHEIRO)
print('Lido (módulo csv):', notas_lidas)
print('Igual ao original?', notas_lidas == notas)

#guardar_csv_manual(notas, 'notas_manual.csv')
#print('Lido (manual):    ', ler_csv_manual('notas_manual.csv'))
