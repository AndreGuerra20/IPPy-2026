# Ficha 8 - Ex 3
# Usando um tuplo, dado o número do mês, indique qual é esse mês e quantos dias tem.


def pedir_numero_mes():
    mes = int(input("Número do mês (1-12): "))
    while mes < 1 or mes > 12:
        print("Mês inválido")
        mes = int(input("Número do mês (1-12): "))
    return mes


def respetivoMes(mes):
    # Criar um tuplo com os nomes dos meses e outro com os dias
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
             "Setembro", "Outubro", "Novembro", "Dezembro")
    dias = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # ou juntar ambos num tuplo aninhado (nested)
    meses_juntos = (("janeiro", 31), ("fevereiro", 28), ("março", 31), ("abril", 30),
                    ("maio", 31), ("junho", 30), ("julho", 31), ("agosto", 31),
                    ("setembro", 30), ("outubro", 31), ("novembro", 30), ("dezembro", 31))

    print(f"O mês {mes} tem {dias[mes - 1]} dias e é o mês {meses[mes - 1]}")
    print(f"O mês {mes} tem {meses_juntos[mes - 1][1]} dias e é o mês {meses_juntos[mes - 1][0]}")


respetivoMes(pedir_numero_mes())
