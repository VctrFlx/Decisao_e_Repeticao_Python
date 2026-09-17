# EXERCICIO 44
# Potência

base = 0.0
expoente = 0
contador = 0
resultado = 1.0

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente inteiro não negativo: "))

if expoente < 0:
    print("Este programa considera apenas expoentes não negativos.")
else:
    for contador in range(1, expoente + 1):
        resultado = resultado * base

    print("Potência:", resultado)