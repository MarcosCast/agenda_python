agenda = {}

while True:
    print("\nAGENDA TELEFÔNICA\n")
    print("1. Adicionar contato")
    print("2. Procurar contato por nome")
    print("3. Editar contato")
    print("4. Ver todos os contatos")
    print("5. Remover contato")
    print("6. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print("\nContato adicionado com sucesso!")

    elif opcao == "2":
        nome = input("\nDigite o nome do contato: ")
        if nome in agenda:
            print("\nTelefone do contato:", agenda[nome])
        else:
            print("\nContato não encontrado.")

    elif opcao == "3":
        nome = input("\nDigite o nome do contato que deseja editar: ")
        if nome in agenda:
            novo_telefone = input("Digite o novo telefone do contato: ")
            agenda[nome] = novo_telefone
            print("\nContato editado com sucesso!")
        else:
            print("\nContato não encontrado.")

    elif opcao == "4":
        if len(agenda) == 0:
            print("\nNão há contatos na agenda.")
        else:
            print("\nLISTA DE CONTATOS")
            for nome, telefone in agenda.items():
                print(nome + " - " + telefone)

    elif opcao == "5":
        nome = input("\nDigite o nome do contato que deseja remover: ")
        if nome in agenda:
            del agenda[nome]
            print("\nContato removido com sucesso!")
        else:
            print("\nContato não encontrado.")

    elif opcao == "6":
        print("\nSaindo da agenda telefônica...")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
