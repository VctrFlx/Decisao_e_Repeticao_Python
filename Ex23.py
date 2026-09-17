# EXERCICIO 23
# Três valores crescentes e um quarto valor

a = 0
b = 0
c = 0
d = 0

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

while b <= a:
    print("O segundo valor deve ser maior que o primeiro")
    b = int(input("Digite novamente o segundo valor: "))

c = int(input("Digite o terceiro valor: "))

while c <= b:
    print("O terceiro valor deve ser maior que o segundo")
    c = int(input("Digite novamente o terceiro valor: "))

d = int(input("Digite o quarto valor: "))

if d < a:
    print(d, a, b, c)
elif d < b:
    print(a, d, b, c)
elif d < c:
    print(a, b, d, c)
else:
    print(a, b, c, d)