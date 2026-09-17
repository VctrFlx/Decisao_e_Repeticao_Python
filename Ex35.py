# EXERCICIO 35
# Soma dos números ímpares entre dois valores

a = 0
b = 0
menor = 0
maior = 0
contador = 0
soma = 0

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a < b:
    menor = a
    maior = b
else:
    menor = b
    maior = a

for contador in range(menor, maior + 1):
    if contador % 2 != 0:
        soma = soma + contador

print("Soma dos ímpares:", soma)