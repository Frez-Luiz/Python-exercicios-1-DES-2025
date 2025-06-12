# Peça três números e exiba-os em ordem crescente.

numero1 = int(input("Digite um número."))
numero2 = int(input("Digite outro número."))
numero3 = int(input("Digite mais um número."))


if numero1 <= numero2 <= numero3:
    print(numero1, numero2, numero3)
elif numero1 <= numero3 <= numero2:
    print(numero1, numero3, numero2)
elif numero2 <= numero1 <= numero3:
    print(numero2, numero1, numero3)
elif numero2 <= numero3 <= numero1:
    print(numero2, numero3, numero1)
elif numero3 <= numero1 <= numero2:
    print(numero3, numero1, numero2)
else:
    print(numero3, numero2, numero1)

#finalizado
