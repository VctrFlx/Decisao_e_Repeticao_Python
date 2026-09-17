# EXERCICIO 41
# Possibilidades de dois dados com soma 7

dado1 = 0
dado2 = 0
soma = 0

for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        soma = dado1 + dado2

        if soma == 7:
            print("Dado 1:", dado1, "Dado 2:", dado2)