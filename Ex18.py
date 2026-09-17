# EXERCICIO 18
# Diferença do maior pelo menor - números inteiros

a = 0.0
b = 0.0
dif = 0.0

a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))

if a > b:
    dif = a - b
else:
    dif = b - a
    
#O else funciona para b>a ou b=a

print("Diferença:", dif)