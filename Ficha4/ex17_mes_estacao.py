# Ficha 4 - Ex 17
# Dado o número de um mês, determine quantos dias tem e a que estação do ano pertence.

mes = int(input("Número do mês (1-12): "))

if 1 <= mes <= 12:
    if mes == 2:
        dias = 28
    elif mes in (4, 6, 9, 11):
        dias = 30
    else:
        dias = 31

    if mes in (12, 1, 2):
        estacao = "Inverno"
    elif mes in (3, 4, 5):
        estacao = "Primavera"
    elif mes in (6, 7, 8):
        estacao = "Verão"
    else:
        estacao = "Outono"

    print(f"O mês {mes} tem {dias} dias e pertence ao {estacao}.")
else:
    print("Mês inválido!")
