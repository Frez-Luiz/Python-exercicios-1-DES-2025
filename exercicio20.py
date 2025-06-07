# Simule um login com nome de usuário "admin" e senha "1234".
# Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado".

nome_correto = "admin"
senha_correta = "1234"

login = input("Digite seu nome de usuário:")
senha = input("Digite sua senha:")

if login == nome_correto and senha == senha_correta:
    print("Acesso concedido.")
else:
    print("Acesso negado.")

    #finalizado