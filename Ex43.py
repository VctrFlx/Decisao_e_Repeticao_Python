# EXERCICIO 43
# Crescimento de Ana e Maria

ana = 1.10
maria = 1.50
crescimento_ana = 0.03
crescimento_maria = 0.02
anos = 0

while ana <= maria:
    ana = ana + crescimento_ana
    maria = maria + crescimento_maria
    anos = anos + 1

print("Anos necessários:", anos)