#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.


tarefaX = int(input("Tempo de entrega da primeira tarefa:"))
tarefaY = int(input("Tempo de entrega da segunda tarefa:"))
tarefaZ = int(input("Tempo de entrega da terceira tarefa:"))
              

if tarefaX < 0 or tarefaY < 0 or tarefaZ < 0:
    print("ERRO! Número negativo.")
else:
    soma = tarefaX + tarefaY + tarefaZ
    print(f"Tempo total da entrega: {soma} ")

    #finalizado