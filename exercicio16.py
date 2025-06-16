# Crie um programa que calcule o reajuste de salário:

# Salários até R$ 2000,00: +15%
# De R$ 2000,01 a R$ 5000,00: +10%
# Acima de R$ 5000,00: +5%


salario = float(input("Digite seu salário."))

reajuste1 = salario*0.15
reajuste2 = salario*0.10
reajuste3 = salario*0.05


if salario <= 2000:
    print("Você ganhou um reajuste de + 15%, que foi de +" , reajuste1)
elif  2000.01 <= salario <= 5000:
    print("Você ganhou um reajuste de + 10%, que foi de +" , reajuste2)
elif salario > 5000:
    print("Você ganhou um reajuste de + 5%, que foi de +" , reajuste3)


#finalizado pela metade