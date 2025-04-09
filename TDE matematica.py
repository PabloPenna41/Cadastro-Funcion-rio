import os
import matplotlib.pyplot as plt

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
print("\033[1;33m=-=-=-=-=-=-=< Mikael Store >=-=-=-=-=-=-=-=")
valor_por_hora = float(input("\033[1;37mDigite o valor da hora trabalhada: "))

funcionarios = []

while True:
    limpar_tela()
    
    print("Menu:\033[1;33m")
    print("1 - Cadastrar Funcionário\033[1;31m")
    print("2 - Mostrar lista de Funcionários\033[1;32m")
    print("3 - Mostrar gráfico de salário de um Funcionário\033[1;35m")
    print("4 - Fechar o programa\033[1;36m")
    
    opcao = input("Digite a opção desejada: ")
    
    match opcao:
        case "1":
            limpar_tela()
            print("\033[1;33m")
            nome = input("Digite o nome do funcionário: ")
            horas = float(input("Digite a quantidade de horas trabalhadas: "))
            salario = horas * valor_por_hora
            funcionarios.append({"nome": nome, "horas": horas, "salario": salario})
            print(f"\nFuncionário {nome} cadastrado com sucesso. Salário: R$ {salario:.2f}")
            input("\nPressione Enter para voltar ao menu...")
        
        case "2":
            limpar_tela()
            if not funcionarios:
                print("\033[1;31mNenhum funcionário cadastrado!")
            else:
                print("Lista de Funcionários:")
                for func in funcionarios:
                    print(f"Nome: {func['nome']}, Horas Trabalhadas: {func['horas']}, Salário: R$ {func['salario']:.2f}")
            input("\nPressione Enter para voltar ao menu...")
        
        case "3":
            limpar_tela()
            if not funcionarios:
                print("\033[1;32m")
                print("\033[1;32mNenhum funcionário cadastrado!")
                input("\nPressione Enter para voltar ao menu...")
            else:
                print("Escolha o funcionário para visualizar o gráfico:")
                for i, func in enumerate(funcionarios):
                    print(f"{i + 1} - {func['nome']}")
                try:
                    escolha = int(input("Digite o número correspondente ao funcionário: ")) - 1
                    
                    if 0 <= escolha < len(funcionarios):
                        nome = funcionarios[escolha]['nome']
                        max_horas = int(funcionarios[escolha]['horas']) + 10
                        
                        horas = list(range(0, max_horas + 1))
                        salarios = [h * valor_por_hora for h in horas]
                        
                        plt.plot(horas, salarios, label=f"Salário de {nome}", color='pink')
                        plt.title(f"Gráfico de Salário - {nome}")
                        plt.xlabel("Horas Trabalhadas")
                        plt.ylabel("Salário (R$)")
                        plt.grid(True)
                        plt.legend()
                        plt.show()
                    else:
                        print("Escolha inválida.")
                        input("\nPressione Enter para voltar ao menu...")
                except ValueError:
                    print("Entrada inválida.")
                    input("\nPressione Enter para voltar ao menu...")
        
        case "4":
            limpar_tela()
            print("\033[1;35m")
            print("\033[1;35mObrigado por vir a Mikael Store, volte sempre!")
            print(" ")
            break
        
        case _:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para voltar ao menu...")
