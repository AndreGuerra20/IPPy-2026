# Ficha 6 - Ex 6
# Função que, dada uma data 'dd/mm/aaaa', devolve a frase 'dd de MM de aaaa'.
# Exemplo: '17/02/2015' -> '17 de Fevereiro de 2015'
# Tem uma função auxiliar que, dado 'mm', devolve o respetivo mês.


def respetivoMes(numMes):
    """Devolve o nome do mês correspondente a numMes ('01' a '12')."""
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
             "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    return meses[int(numMes) - 1]


def dataNascimento(data):
    """Converte 'dd/mm/aaaa' em 'dd de <Mês> de aaaa'."""
    dia, mes, ano = data.split("/")
    return f"{dia} de {respetivoMes(mes)} de {ano}"


print(dataNascimento("17/02/2015"))
