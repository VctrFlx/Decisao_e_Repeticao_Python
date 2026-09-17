# EXERCICIO 22
# Dois valores em ordem crescente

a = 0
b = 0

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a > b:
    print(a, b)
elif b > a:
    print(b, a)
else:
    print("Números iguais")