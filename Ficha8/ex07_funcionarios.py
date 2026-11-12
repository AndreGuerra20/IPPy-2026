# Ficha 8 - Ex 7
# Construa o tuplo com os funcionários de uma empresa até que o utilizador escreva "fim".
# Cada funcionário: (nome, idade, ordenado, categoria), categoria em 'A', 'B', 'C', 'D'.

CATEGORIAS = ('A', 'B', 'C', 'D')
AUMENTOS = (8, 7.5, 5, 3)            # % por categoria
DIVIDENDOS = (190, 225, 250, 300)    # € mensais por categoria


def ler_funcionarios():
    funcionarios = ()
    nome = input('Nome (fim para terminar): ')
    while nome.lower() != 'fim':
        idade = int(input('  Idade: '))
        ordenado = float(input('  Ordenado: '))
        categoria = input('  Categoria (A/B/C/D): ').upper()
        while categoria not in CATEGORIAS:
            categoria = input('  Categoria inválida (A/B/C/D): ').upper()
        funcionarios += ((nome, idade, ordenado, categoria),)
        nome = input('Nome (fim para terminar): ')
    return funcionarios


def idade(funcionario):
    """Função usada como chave de ordenação (sorted(..., key=idade))."""
    return funcionario[1]


def categoria(funcionario):
    return funcionario[3]


def mostrar(funcionarios):
    for nome, idade_f, ordenado, cat in funcionarios:
        print(f'  {nome:<20} {idade_f:>3} anos  {ordenado:>9.2f} €  {cat}')


# a) Por ordem alfabética
def alinea_a(funcionarios):
    print('a) Por ordem alfabética')
    mostrar(tuple(sorted(funcionarios)))


# b) Por ordem decrescente das idades + contagem por faixa etária
def alinea_b(funcionarios):
    print('b) Por ordem decrescente das idades')
    mostrar(tuple(sorted(funcionarios, key=idade, reverse=True)))
    menos30 = 0
    de30a45 = 0
    de45a55 = 0
    mais55 = 0
    for f in funcionarios:
        if f[1] < 30:
            menos30 += 1
        elif f[1] < 45:
            de30a45 += 1
        elif f[1] < 55:
            de45a55 += 1
        else:                      # 55 ou mais
            mais55 += 1
    print('  Menos de 30 anos:', menos30)
    print('  Entre 30 e menos de 45:', de30a45)
    print('  Entre 45 e menos de 55:', de45a55)
    print('  55 ou mais anos:', mais55)


# c) Por categoria, com aumento, dividendo e ordenado final + massa salarial
def alinea_c(funcionarios):
    print('c) Por categoria')
    massa_atual = 0
    massa_futura = 0
    print(f'  {"Nome":<20} {"Cat":>3} {"Atual":>9} {"Aumento":>9} {"Dividendo":>9} {"Final":>9}')
    for nome, idade_f, ordenado, cat in sorted(funcionarios, key=categoria):
        indice = CATEGORIAS.index(cat)
        aumento = ordenado * AUMENTOS[indice] / 100
        dividendo = DIVIDENDOS[indice]
        final = ordenado + aumento + dividendo
        massa_atual += ordenado
        massa_futura += final
        print(f'  {nome:<20} {cat:>3} {ordenado:>9.2f} {aumento:>9.2f} {dividendo:>9.2f} {final:>9.2f}')
    print(f'  Massa salarial atual: {massa_atual:.2f} €')
    print(f'  Aumento da massa salarial futura: {massa_futura - massa_atual:.2f} €')


funcionarios = ler_funcionarios()
alinea_a(funcionarios)
alinea_b(funcionarios)
alinea_c(funcionarios)
