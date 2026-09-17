# EXERCICIO 19
# Diferença do maior pelo menor - números reais

a = 0.0
b = 0.0
dif = 0.0

a = float(input("Digite o primeiro valor real: "))
b = float(input("Digite o segundo valor real: "))

if a > b:
    dif = a - b
else:
    dif = b - a
    
#O else funciona para b>a ou b=a

print("Diferença:", dif)