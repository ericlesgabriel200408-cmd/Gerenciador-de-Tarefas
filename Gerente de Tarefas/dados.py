## Dados usados no projeto

tarefas = []            #lista: armazena todas tarefas
fila_pedente = []       #fila (FIFO): armazena as tarefas que estão pendentes
pilha_concluida = []    #pilha (LIFO): armazenaas tarefas concluídas
em_andamento = []       #lista: armazena as tarefas que estão em andamento

prioridades = ('Baixa' , 'Média' , 'Alta') #tupla: define as prioridades disponíveis para as tarefas
status = ('Pendente' , 'Em Andamento' , 'Concluída') #tupla: define os status disponíveis para as tarefas
