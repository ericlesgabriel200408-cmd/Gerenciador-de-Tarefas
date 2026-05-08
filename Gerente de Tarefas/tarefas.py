from  dados import tarefas, fila_pendente, pilha_concluida, em_andamento, prioridade, status
from utils import titulo

def cadastrar_tarefa():
    titulo('Cadastrar Tarefa')
    
    descricao = input('Descrição: ')
    disciplina = input('Disciplina: ')
    data_entrega = input('Data de Entrega (dd/mm/aaaa): ')
    
    print(' - Prioridade: 1. Baixa  2. Média  3. Alta')
    opcao = input('Escolha a prioridade: ')
    if opcao == '1':
        prioridades = prioridade [0]
    
    elif opcao == '2':
        prioridades = prioridade [1]
    
    else:
        print('Opção inválida. Prioridade definida como Baixa.')
        prioridades = prioridade [2]
        
    dict_tarefas = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'disciplina': disciplina,
        'data_entrega': data_entrega,
        'prioridade': prioridade,
        'status': status [0]
    }
    tarefas.append(dict_tarefas)
    fila_pendente.append(dict_tarefas)
print('Tarefa cadastrada com sucesso!')

def listar_tarefas():
    titulo('Listar Tarefas')
    
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'TAREFA: {i}')
        print(f'ID: {tarefa['id']}')
        print(f'Descrição: {tarefa['descricao']}')
        print(f'Disciplina: {tarefa['disciplina']}')
        print(f'Data de Entrega: {tarefa['data_entrega']}')
        print(f'Prioridade:{tarefa['prioridade']}')
        print(f'Status: {tarefa['status']}')
        print()
        
def atualizar_status():
    print('\n === Atualizar Status ===')
    listar_tarefas()
            
    if len(tarefas) == 0:   #se não houver tarefas cadastradas, não faz sentido tentar atualizar o status.
        return              # Assim , evitamos que o usuário tente atualizar uma tarefa inexistente
            
        try:
            id_tarefa = int(input('Digite o id da tarefa: '))
        except VallueError:             #se o usuário digitar algo que não seja número inteiro, isso causaria um erro.
            print('Digite um número válido.')
            return
            
            for tarefa in tarefas:
                if tarefa['id'] == id_tarefas:
                    print('\nEscolha o novo status:')
                    print('1 - Pendente')
                    print('2 - Em andamento')
                    print('3 - Concluída')
                    opcao = input('Opção: ')
                    
                    if opcao == '1':
                        tarefa['status'] = status[0]
                        if tarefa not in fila_pendente:
                            fila_pendente.append(tarefa)
                    elif opcao == '2':
                        tarefa['status'] = status [1]
                    elif opcao == '3':
                        tarefa['status'] = status [2]
                        pilha_concluida.append(tarefa)
                        if tarefa in fila_pendente:
                            fila_pendente.remove(tarefa)
                    else:
                        print('Opção inválida.')
                        return
                    
                    print('Status atualizado com successo!')
                    return
    print('Tarefa não encontrada.')
    
    
    def ver_historico_concluidas():
        titulo('Histórico de Tarefas Concluídas')
        if len(pilha_concluida) == 0:
            print('Nenhuma tarefa concluída.')
            return
        
        #Usamos reversed() para mostrar as tarefas do topo da pilha para baixo.
        #Ou seja, a tarefa mais recentemente concluída aparecerá primeiro, seguida pelas tarefas concluídas anteriormente.
        for i, tarefa in enumerate(reversed(pilha_concluida), start=1):
            print(f'TAREFA CONCLUÍDA: {i}')
            print(f'ID: {tarefa['id']}')
            print(f'Descrição: {tarefa['descricao']}')
            print(f'Disciplina: {tarefa[disciplina]}')
            print(f'Data de Entrega: {tarefa[data_entrega]}')
            print(f'Prioridade: {tarefa[prioridade]}')
            print()