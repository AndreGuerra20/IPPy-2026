# Ficha 5 - Ex 14
# Enquanto o utilizador não digitar '.', '!' ou '?', vá pedindo um caracter. No final,
# apresente a frase composta por todos os caracteres digitados.

simbolos = ".!?"
string_final = ""
char = input("Insira 1 caracter: ")
# len(char) != 1 evita que um Enter vazio termine o ciclo ("" in simbolos é True)
while len(char) != 1 or char not in simbolos:
    if len(char) == 1:
        string_final += char
    else:
        print("Só pode inserir 1 caracter")

    char = input("Insira 1 caracter: ")

print(string_final + char)
