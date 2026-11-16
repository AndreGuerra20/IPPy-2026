import temperaturas

celsius = float(input("Digite a temperatura em Celsius: "))
print(f"{celsius}ºC = {temperaturas.celsius_para_fahrenheit(celsius)} ºF ({temperaturas.classificar(celsius)})")