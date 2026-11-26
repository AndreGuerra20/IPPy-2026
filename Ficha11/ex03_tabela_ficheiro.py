# Ficha 11 - Ex 3
# Tabela nome / numero / nota / status:
# a) colocar a informação numa lista de listas
# b) mostrar a estrutura no ecrã
# c) guardar num ficheiro de texto
# d) ler o ficheiro para uma lista de listas

NOME_FICHEIRO = 'alunos.txt'
SEPARADOR = '\t'


# a)
def criar_tabela():
    return [['nome', 'numero', 'nota', 'status'],
            ['antonio', 1001, 12, 'aprovado'],
            ['maria', 1023, 16, 'aprovado'],
            ['ze', 1010, 8, 'reprovado']]


# b)
def mostrar_tabela(tabela):
    for linha in tabela:
        print(f'{linha[0]:<10}{linha[1]:>8}{linha[2]:>6}  {linha[3]:<10}')


# c) cada linha da tabela é uma linha do ficheiro, com os campos separados por tab
def guardar_tabela(tabela, nome_ficheiro):
    with open(nome_ficheiro, 'w', encoding='utf-8') as ficheiro:
        for linha in tabela:
            ficheiro.write(str(linha[0]) + SEPARADOR + str(linha[1]) + 
                           SEPARADOR + str(linha[2]) + SEPARADOR + str(linha[3]) + '\n')


# d) os números voltam a ser convertidos para int (exceto na linha do cabeçalho)
def ler_tabela(nome_ficheiro):
    tabela = []
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        for linha in ficheiro:
            campos = linha.split(SEPARADOR)
            if len(tabela) > 0:
                # converter os campos 1 e 2 para int
                campos[1] = int(campos[1])
                campos[2] = int(campos[2])
            
            # remover o '\n' do último campo
            campos[3] = campos[3].strip()
            
            # Adicionar a linha à tabela
            tabela.append(campos)
    return tabela


dados = criar_tabela()
mostrar_tabela(dados)
guardar_tabela(dados, NOME_FICHEIRO)
print('Guardado em', NOME_FICHEIRO)
dados_lidos = ler_tabela(NOME_FICHEIRO)
print('Lido do ficheiro:', dados_lidos)
print('Igual ao original?', dados_lidos == dados)
