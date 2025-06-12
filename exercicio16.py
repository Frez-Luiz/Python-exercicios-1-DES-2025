# Crie um programa que calcule o reajuste de salário:

# Salários até R$ 2000,00: +15%
# De R$ 2000,01 a R$ 5000,00: +10%
# Acima de R$ 5000,00: +5%


salario = float(input("Digite seu salário."))

reajuste1 = salario*0.15
reajuste2 = salario*0.10
reajuste3 = salario*0.05


if salario <= 2000:
    print("Você ganhou um reajuste de + 15%.")
