from dados import tarefas, fila_pedente, pilha_concluida, em_andamento, prioridades, status
from utils import titulo
from tarefas import cadastrar_tarefa

def mostrar_menu():
    titulo('Gerenciador de Tarefas')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Sair')

while True:
    mostrar_menu()
    
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_tarefa()
    elif opcao == '2':
        print('opção 2 selecionada')
    elif opcao == '3':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
