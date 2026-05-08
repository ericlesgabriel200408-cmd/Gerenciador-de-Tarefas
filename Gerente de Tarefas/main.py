from dados import tarefas, fila_pendente, pilha_concluida, em_andamento, prioridade, status
from utils import titulo
from tarefas import cadastrar_tarefa, listar_tarefas, atualizar_status

def mostrar_menu():
    titulo('Gerenciador de Tarefas')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3, Atualizar Status')
    print('4. Sair')

while True:
    mostrar_menu()
    
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_tarefa()
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        atualizar_status()
    elif opcao == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
