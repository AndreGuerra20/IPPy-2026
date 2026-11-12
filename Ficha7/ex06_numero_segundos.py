# Ficha 7 - Ex 6
# Dado o valor das horas, minutos e segundos no formato "hh:mm:ss", determine e apresente
# o número de segundos correspondentes.


def numero_segundos(horas_minutos_segundos):
    horas, minutos, segundos = horas_minutos_segundos.split(":")
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos)


print(numero_segundos("23:59:59"))
print(numero_segundos(input('Tempo (hh:mm:ss): ')))
