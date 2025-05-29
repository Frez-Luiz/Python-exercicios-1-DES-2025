#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
# Soma ok, só não funciona o negativo.

tarefaX = int(input("Digite o tempo da tarefa X."))
tarefaY = int(input("Digite o tempo da tarefa Y."))
tarefaZ = int(input("Digite o tempo da tarefa Z."))
              
soma = tarefaX + tarefaY + tarefaZ
if tarefaX  < 0:
    print("ERRO! Seu tempo foi negativo.")
elif tarefaY  < 0:
    print("ERRO! Seu tempo foi negativo.")
elif tarefaZ  < 0:
    print("ERRO! Seu tempo foi negativo.")
else:
    print("Seu tempo foi:" , soma)
    