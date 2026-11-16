from temperaturas import *

fahrenheit = float(input("Temperatura em ºF: "))
print(f"{fahrenheit}ºF = {fahrenheit_para_celsius(fahrenheit)} ºC ({classificar(fahrenheit_para_celsius(fahrenheit))})")