
# validador de senha correta

senhaCorreta = "123456"
senha = input("Digite a senha: ")

while senha != senhaCorreta:
    print("Senha incorreta")
    senha = input ("Tente novamente: ")
print ("Acesso permitido!!")

#pronto