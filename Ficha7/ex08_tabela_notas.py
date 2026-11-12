# Ficha 7 - Ex 8
# Mostrar a estrutura nt no ecrã em forma de tabela:
# (a) com uma linha separadora entre todas as linhas
# (b) com linha separadora só depois do cabeçalho e no fim

nt = (('Nome', 'Teste 1', 'Teste 2', 'Teste 3'),
      ('Joaquim Silva', '10', '14', '12'),
      ('Maria Antonia', '11', '8', '18'),
      ('Jose Carlos', '14', '10', '10'))

LARGURA_NOME = 14
LARGURA_NOTA = 7


def linha_separadora():
    """Devolve a linha +----+----+ com as larguras das colunas."""
    return '+' + '-' * LARGURA_NOME + ('+' + '-' * LARGURA_NOTA) * 3 + '+'


def linha_cabecalho(cabecalho):
    texto = '|' + cabecalho[0].ljust(LARGURA_NOME)
    for titulo in cabecalho[1:]:
        texto += '|' + titulo.rjust(LARGURA_NOTA)
    return texto + '|'


def linha_aluno(aluno):
    """Nome alinhado à esquerda e notas alinhadas à direita."""
    texto = '|' + aluno[0].ljust(LARGURA_NOME)
    for nota in aluno[1:]:
        texto += '|' + nota.rjust(LARGURA_NOTA)
    return texto + '|'


def tabela_a(dados):
    print(linha_separadora())
    print(linha_cabecalho(dados[0]))
    print(linha_separadora())
    for aluno in dados[1:]:
        print(linha_aluno(aluno))
        print(linha_separadora())


def tabela_b(dados):
    print(linha_separadora())
    print(linha_cabecalho(dados[0]))
    print(linha_separadora())
    for aluno in dados[1:]:
        print(linha_aluno(aluno))
    print(linha_separadora())


print('(a)')
tabela_a(nt)
print()
print('(b)')
tabela_b(nt)
