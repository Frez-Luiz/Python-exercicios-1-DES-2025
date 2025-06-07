# Loja oferece os seguintes descontos:

# Compras acima de R$ 500,00 têm 10%
# Acima de R$ 300,00 têm 5%
# Menor ou igual a R$ 300,00 não têm desconto

compras = float(input("Digite o valor da sua compra."))

if compras > 500:
    print("Você tem 10% de desconto.")
elif compras > 300 < 500:
    print("Você tem apenas 5% dedesconto.")
elif compras <= 300:
    print("Você não tem descontos")

    #finalizado