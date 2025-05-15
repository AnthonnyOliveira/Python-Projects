from src.cli.menu import exibir_menu

if __name__ == "__main__":
    exibir_menu()

def exibir_menu():
    print("\n=== SISTEMA DE CONTROLE DE ACADEMIA ===")
    print("1. Cadastrar Aluno")
    print("2. Registrar Entrada")
    print("3. Registrar Saída")
    print("4. Relatórios")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    print(f"Você escolheu a opção {opcao}")
