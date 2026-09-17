# EXERCICIO 26
# Verificar se o maior é múltiplo do menor

a = 0
b = 0
maior = 0
menor = 0

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

if menor != 0 and maior % menor == 0:
    print("O maior é múltiplo do menor.")
else:
    print("O maior não é múltiplo do menor ou o menor é zero.")