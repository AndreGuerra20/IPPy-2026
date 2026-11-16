import random
print('Módulo temperaturas carregado!')

def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def classificar(celsius):
    """ Classifica a temperatura em Celsius 'Frio' se for inferior a 10 ºC, 
    'Ameno' se for inferior a 25 ºC e 'Quente' nos restantes casos"""
    if celsius < 10:
        return "Frio"
    elif celsius < 25:
        return "Ameno"
    else:
        return "Quente"
    
def gerar_temperaturas(n):
    """Gera uma lista com n temperaturas aleatórias em ºC, entre -5 e 40, com uma casa decimal"""
    temperaturas = []
    for i in range(n):
        nova_temp = random.uniform(-5, 40)
        temp_1_casa_decimal = round(nova_temp, 1)
        temperaturas.append(temp_1_casa_decimal)
    return temperaturas