import os

class Menu:
    def __init__(self):
        pass

    def MenuPrincipal(self):
        os.system('clear')
        print("\nMenu Principal:")
        print("1. Analisar Hardware")
        print("2. Aplicativos")
        print("3. Repositórios")
        print("4. Informações")
        print("5. Sair do Linux")
        return int(input("Escolha uma opção: "))

    def MenuHardware(self):
        os.system('clear')
        print("\nMenu de Hardware:")
        print("1. Analisar Saúde")
        print("2. Uso da CPU")
        print("3. Memória")
        print("4. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Faltou implementar as funções

    def MenuApp(self):
        os.system('clear')
        print("\nMenu de Aplicativos:")
        print("1. Listar aplicativos instalados")
        print("2. Instalar aplicativos")
        print("3. Iniciar aplicativo")
        print("4. Permissões do aplicativo")
        print("5. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Faltou implementar as funções

    def MenuRepository(self):
        os.system('clear')
        print("\nMenu de Repositórios:")
        print("1. Listar repositórios (e seus pacotes)")
        print("2. Pacotes existentes")
        print("3. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Faltou implementar as funções

    def MenuInfo(self):
        os.system('clear')
        print("\nMenu de Informações:")
        print("1. Máquina (Listar informações da máquina)")
        print("2. Servidor (Listar informações do servidor)")
        print("3. Arquitetura de Software (Listar informações da arquitetura de software)")
        print("4. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))

        while self.MenuInfo:
            if choice == 1:
                self.lists.MachineInfo(self.machine)
            elif choice == 2:
                self.lists.ServerInfo(self.server)
            elif choice == 3:
                self.lists.ArchitectureInfo(self.software_architecture)
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
            choice = int(input("Escolha uma opção: "))  
