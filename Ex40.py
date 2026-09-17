# EXERCICIO 40
# Números primos entre dois valores

a = 0
b = 0
menor = 0
maior = 0
numero = 0
divisor = 0
quantidade_divisores = 0

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a < b:
    menor = a
    maior = b
else:
    menor = b
    maior = a

for numero in range(menor, maior + 1):
    if numero >= 2:
        quantidade_divisores = 0

        for divisor in range(1, numero + 1):
            if numero % divisor == 0:
                quantidade_divisores = quantidade_divisores + 1

        if quantidade_divisores == 2:
            print(numero)