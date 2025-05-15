def exibir_menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar aluno")
        print("2. Registrar entrada")
        print("3. Registrar saída")
        print("4. Gerar relatórios")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Função de cadastro de aluno aqui")
        elif opcao == "2":
            print("Função de registro de entrada aqui")
        elif opcao == "3":
            print("Função de registro de saída aqui")
        elif opcao == "4":
            print("Função de relatórios aqui")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
