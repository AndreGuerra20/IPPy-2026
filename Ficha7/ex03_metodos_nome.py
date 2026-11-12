# Ficha 7 - Ex 3 (igual à Ficha 3 - 3.3 Ex 3)
# Inicialize a variável nome com o seu nome completo e resolva em Python.

nome = "André Miguel Raposo Guerra"

# a) O nome tem a palavra 'de'?
print("(a)", "de" in nome)

# b) Maior e menor elemento do nome
print(f"(b) Maior elemento do meu nome é: '{max(nome)}'")
print("(b) Menor elemento do meu nome é: '", min(nome), "'", sep='')

# c) Número de vezes que aparece a vogal 'o'
print("(c)", nome.count('o'))

# d) Nome em maiúsculas
print("(d)", nome.upper())

# e) Nome sem espaços em branco (strip só remove os espaços das pontas)
print("(e)", nome.replace(" ", ""))

# f) Substituir a vogal 'e' por 'U'
print("(f)", nome.replace("e", "U"))

# g) Termina com a letra 's'?
print("(g)", nome.endswith("s"))

# h) Índice da primeira ocorrência de 'da' (find devolve -1 se não existir;
#    index daria erro)
print("(h)", nome.find("da"))

# i) Nome em minúsculas pela ordem inversa
print("(i)", nome.lower()[::-1])

# j) Nome centrado numa string de comprimento 80
print("(j)", nome.center(80))

# k) Separar o nome por palavras
print("(k)", nome.split())

# l) Número de vezes que aparece a vogal 'a'
print("(l)", nome.count("a"))
