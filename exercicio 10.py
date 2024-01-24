class CalendarioTarefas:
    def __init__(self):
        self.calendario = {}

    def adicionar_tarefa(self, data, tarefa):
        if data in self.calendario:
            self.calendario[data].append(tarefa)
            print(f'Tarefa adicionada em {data}: {tarefa}')
        else:
            self.calendario[data] = [tarefa]
            print(f'Tarefa adicionada em {data}: {tarefa}')

    def editar_tarefa(self, data):
        if data in self.calendario:
            print(f'Tarefas em {data}: {", ".join(self.calendario[data])}')
            indice = int(input('Digite o número da tarefa que deseja editar: ')) - 1

            if 0 <= indice < len(self.calendario[data]):
                nova_tarefa = input('Digite a nova descrição da tarefa: ')
                self.calendario[data][indice] = nova_tarefa
                print(f'Tarefa editada em {data}: {nova_tarefa}')
            else:
                print('Número de tarefa inválido.')
        else:
            print('Data inválida. Certifique-se de digitar corretamente.')

    def mostrar_calendario(self):
        for data, tarefas in self.calendario.items():
            print(f'{data}: {", ".join(tarefas)}')

# Criar uma instância do CalendarioTarefas
calendario = CalendarioTarefas()

# Loop para interação com o usuário
while True:
    print("\n=== Menu ===")
    print("1. Adicionar Tarefa")
    print("2. Editar Tarefa")
    print("3. Mostrar Calendário")
    print("4. Sair")

    escolha = input('Escolha uma opção (1/2/3/4): ')

    if escolha == '1':
        data = input('Digite a data (formato YYYY-MM-DD): ')
        tarefa = input('Digite a tarefa: ')
        calendario.adicionar_tarefa(data, tarefa)

    elif escolha == '2':
        data = input('Digite a data da tarefa a ser editada (formato YYYY-MM-DD): ')
        calendario.editar_tarefa(data)

    elif escolha == '3':
        calendario.mostrar_calendario()

    elif escolha == '4':
        break

    else:
        print('Escolha inválida. Tente novamente.')
3