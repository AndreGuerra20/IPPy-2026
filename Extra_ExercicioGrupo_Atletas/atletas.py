# Exercício de grupo - Resultados de uma corrida (Testes/exercicio_grupo.txt)
# Tuplo de tuplos (dorsal, nome, tempo). Só se usam tuplos (sem listas nem dicionários).


# a) Converte um tempo "hh:mm:ss" em segundos
def tempo_em_segundos(t):
    horas, minutos, segundos = t.split(":")
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos)


# a) Converte segundos num tempo "hh:mm:ss"
def segundos_em_tempo(seg):
    horas = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = seg % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


# b) Devolve True se o tempo tiver o formato hh:mm:ss, só com algarismos,
#    e minutos e segundos inferiores a 60
def tempo_valido(t):
    partes = t.split(":")
    if len(partes) != 3:
        return False
    horas, minutos, segundos = partes
    if not (len(horas) == 2 and len(minutos) == 2 and len(segundos) == 2):
        return False
    if horas.isdigit() and minutos.isdigit() and segundos.isdigit():
        if int(minutos) < 60 and int(segundos) < 60:
            return True
    return False


# c) Devolve (melhor, pior, media) em hh:mm:ss, sem usar min, max nem sum.
#    Só os tempos válidos entram nas contas.
def estatisticas(atletas):
    melhor = float('inf')
    pior = 0
    total = 0
    quantidade = 0
    for atleta in atletas:
        tempo = atleta[2]
        if tempo_valido(tempo):
            segundos = tempo_em_segundos(tempo)
            if segundos < melhor:
                melhor = segundos
            if segundos > pior:
                pior = segundos
            total += segundos
            quantidade += 1
    if quantidade == 0:
        return ("--:--:--", "--:--:--", "--:--:--")
    media = total // quantidade
    return (segundos_em_tempo(melhor), segundos_em_tempo(pior), segundos_em_tempo(media))


# d) Devolve um novo tuplo com o atleta acrescentado (ou o original, se houver erro)
def adicionar(atletas, dorsal, nome, tempo):
    if not tempo_valido(tempo):
        print("Tempo inválido, por favor insira o tempo no formato 'hh:mm:ss'")
        print("O Atleta não foi adicionado!")
        return atletas
    if dorsal in (atleta[0] for atleta in atletas):
        print(f"Atleta com dorsal {dorsal} já existe")
        print("O Atleta não foi adicionado!")
        return atletas
    return atletas + ((dorsal, nome, tempo),)


# e) Mostra o menu
def print_menu():
    print("")
    print("    ============ Menu ============")
    print("   1. Listar os atletas numa tabela alinhada.")
    print("   2. Adicionar um atleta, pedindo os dados ao utilizador.")
    print("   3. Mostrar as estatísticas.")
    print("   0. Sair.")
    print("")


# e) Pede uma opção válida do menu
def pedir_opcao():
    opcao = input("Escolha uma opção: ")
    while opcao not in ("0", "1", "2", "3"):
        print("Opção inválida!")
        opcao = input("Escolha uma opção: ")
    return int(opcao)


# e) Pede um dorsal válido (número inteiro)
def pedir_dorsal():
    dorsal = input("Dorsal: ")
    while not dorsal.isdigit():
        print("O dorsal tem de ser um número inteiro!")
        dorsal = input("Dorsal: ")
    return int(dorsal)


# e) Lista os atletas numa tabela alinhada
def listar_atletas(atletas):
    if not atletas:
        print("Não há atletas para mostrar.")
        return

    # largura da coluna do nome ajusta-se ao nome mais comprido
    largura_nome = max(15, max(len(str(a[1])) for a in atletas))

    linha = f"+{'-' * 7}+{'-' * (largura_nome + 2)}+{'-' * 12}+"

    print(linha)
    print(f"| {'Nº':<5} | {'Nome':<{largura_nome}} | {'Tempo':>10} |")
    print(linha.replace('-', '='))
    for atleta in atletas:
        print(f"| {atleta[0]:<5} | {atleta[1]:<{largura_nome}} | {atleta[2]:>10} |")
    print(linha)
    print(f"Total: {len(atletas)} atletas")


# e) Programa
def programa():
    atletas = ((101, "Ana", "00:42:15"),
               (102, "Bruno", "00:39:58"),
               (103, "Carla", "00:51:30"),
               (104, "Diogo", "00:47:02"),
               (105, "Eva", "00:44:40"),
               (106, "Filipe", "00:41:09"),
               (107, "Gabriela", "00:55:47"),
               (108, "Hugo", "00:38:21"),
               (109, "Inês", "00:49:12"),
               (110, "João", "01:02:33"),
               (111, "Kátia", "00:46:05"),
               (112, "Luís", "00:43:50"),
               (113, "Marta", "00:52:18"),
               (114, "Nuno", "00:40:44"),
               (115, "Olga", "00:58:09"))
    print_menu()
    opcao = pedir_opcao()
    while opcao != 0:
        if opcao == 1:
            listar_atletas(atletas)
        elif opcao == 2:
            dorsal = pedir_dorsal()
            nome = input("Nome: ")
            tempo = input("Tempo (hh:mm:ss): ")
            atletas = adicionar(atletas, dorsal, nome, tempo)
        elif opcao == 3:
            melhor, pior, media = estatisticas(atletas)
            print(f"Melhor tempo: {melhor} | Pior tempo: {pior} | Média: {media}")
        print_menu()
        opcao = pedir_opcao()


programa()
