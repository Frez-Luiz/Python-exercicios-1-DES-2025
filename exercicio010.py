# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário


salario = float(input("Digite seu salário mensal:"))
parcela = float(input("Digite qual é a parcela mensal:"))


if salario < 3000:
    print("ERRO! Impossível fazer um financiamento.")
elif parcela > salario*0.35:
    print("Parcela maior que 35% de seu salário")
else:
    print("Financiamento consedido.")

#finalizado