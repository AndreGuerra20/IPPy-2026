# Ficha 7 - Ex 7
# Função que, dado o nome completo, devolve apenas o primeiro nome e o último apelido.


def primeiro_ultimo(nome_completo):
    nomes = nome_completo.split()
    return nomes[0] + ' ' + nomes[-1]


def primeiro_ultimo_sem_split(nome_completo):
    """Alternativa com find/rfind (posição do primeiro e do último espaço)."""
    nome = nome_completo.strip()
    primeiro_espaco = nome.find(' ')
    ultimo_espaco = nome.rfind(' ')
    if primeiro_espaco == -1:          # só tem um nome
        return nome
    return nome[:primeiro_espaco] + nome[ultimo_espaco:]


print(primeiro_ultimo('André Miguel Raposo Guerra'))
print(primeiro_ultimo_sem_split('André Miguel Raposo Guerra'))
