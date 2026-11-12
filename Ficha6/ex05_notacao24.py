# Ficha 6 - Ex 5
# Função que converte as horas da notação de 12 horas para a notação de 24 horas.
# Exemplos: '3:35pm' -> '15:35', '7:18am' -> '7:18', '11:01am' -> '11:01'


def notacao24(notacao12):
    """Converte 'h:mmam'/'h:mmpm' para 'h:mm' na notação de 24 horas."""
    sufixo = notacao12[-2:].lower()            # garantir "am" ou "pm"
    horas, minutos = notacao12[:-2].split(":")
    horas = int(horas)

    if sufixo == "am":
        if horas == 12:        # 12:xx am -> 0:xx
            horas = 0
    else:  # pm
        if horas != 12:        # 12:xx pm fica 12:xx
            horas += 12

    return str(horas) + ":" + minutos


print(notacao24("12:00am"))
print(notacao24("11:01am"))
print(notacao24("7:18am"))
print(notacao24("3:35pm"))
