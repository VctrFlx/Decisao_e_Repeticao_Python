# EXERCICIO 29
# Investimento

tipo = 0
valor = 0.0
valor_corrigido = 0.0

tipo = int(input("Tipo de investimento (1-poupança / 2-renda fixa): "))
valor = float(input("Valor investido: "))

if tipo == 1:
    valor_corrigido = valor + valor * 0.03
elif tipo == 2:
    valor_corrigido = valor + valor * 0.05
else:
    valor_corrigido = valor
    print("Tipo de investimento não considerado.")

print("Valor corrigido:", valor_corrigido)