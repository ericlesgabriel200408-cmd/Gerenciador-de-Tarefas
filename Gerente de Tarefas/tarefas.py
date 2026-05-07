from dados import tarefas, fila_pedente, pilha_concluida, em_andamento, prioridade, status
from utils import titulo

def cadastrar_tarefa():
    titulo('Cadastrar Tarefa')
    
    descricao = input('Descrição: ')
    disciplina = input('Disciplina: ')
    data_entrega = input('Data de Entrega (dd/mm/aaaa): ')
    
    print(' - Prioridade: 1. Baixa  2. Média  3. Alta')
    opcao = input('Escolha a prioridade: ')
    if opcao == '1':
        prioridade = prioridade [0]
    elif opcao == '2':
        prioridade = prioridade [1]
    else:
        print('Opção inválida. Prioridade definida como Baixa.')
        prioridade = prioridade [2]
        
        dict_tarefa = {
            'id': len(tarefas) + 1,
            'descricao': descricao,
            'disciplina': disciplina,
            'data_entrega': data_entrega,
            'prioridade': prioridade,
            'status': status [0]
        }

tarefas.append(dict_tarefa)
fila_pedente.append(dict_tarefa)

print('Tarefa cadastrada com sucesso!')