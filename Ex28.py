# EXERCICIO 28
# Novo preço do produto

preco_atual = 0.0
venda_mensal = 0
preco_novo = 0.0

preco_atual = float(input("Preço atual: "))
venda_mensal = int(input("Média mensal de vendas: "))

preco_novo = preco_atual

if venda_mensal < 500 and preco_atual < 30:
    preco_novo = preco_atual + preco_atual * 0.10
elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
    preco_novo = preco_atual + preco_atual * 0.15
elif venda_mensal >= 1000 and preco_atual >= 80:
    preco_novo = preco_atual - preco_atual * 0.05

print("Novo preço:", preco_novo)