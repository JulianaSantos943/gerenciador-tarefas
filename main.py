from database import criar_tabela, criar_tarefa, listar_tarefa, concluir_tarefa, deletar_tarefa

while True:
    print("1 - Adicionar tarefa")
    print("2 - listar tarefa")
    print("3 - concluir tarefa")
    print("4 - deletar tarefa")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input('Digite o título da tarefa: ')
        criar_tarefa(titulo)
        print('Tarefa adicionada com sucesso!')
    elif escolha == "2":
        listar_tarefa()
    elif escolha == "3":
        listar_tarefa()
        id_tarefa = input('Digite o ID da tarefa a concluir: ')
        resultado = concluir_tarefa(id_tarefa)
        if resultado == 0:
            print('Nenhuma tarefa encontrada com esse ID.')
        else:
            print('Tarefa concluída com sucesso!')
    elif escolha == "4":
        listar_tarefa()
        id_tarefa = input('Digite o ID da tarefa a deletar: ')
        resultado = deletar_tarefa(id_tarefa)
        if resultado == 0:
            print('Nenhuma tarefa encontrada com esse ID.')
        else:
            print('Tarefa deletada com sucesso!')
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Tente novamente")
