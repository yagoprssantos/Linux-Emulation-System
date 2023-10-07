import os
from refresh import Refresh
from machine import Machine
from server import Server
from architecture import SoftwareArchitecture

class Menu:
    def __init__(self):
        self.refresh = Refresh()
        self.machine = Machine()
        self.server = Server()
        self.software_architecture = SoftwareArchitecture()

    def MenuPrincipal(self):
        self.refresh.Fresh()
        print("\nMenu Principal:")
        print("1. Analisar Hardware")
        print("2. Aplicativos")
        print("3. Repositórios")
        print("4. Informações")
        print("5. Sair do Linux")
        return int(input("Escolha uma opção: "))

    def MenuHardware(self):
        self.refresh.Fresh()
        print("\nMenu de Hardware:")
        print("1. Analisar Saúde")
        print("2. Uso da CPU")
        print("3. Memória")
        print("4. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Implemente as funções correspondentes a cada opção do menu

    def MenuApp(self):
        self.refresh.Fresh()
        print("\nMenu de Aplicativos:")
        print("1. Listar aplicativos instalados")
        print("2. Instalar aplicativos")
        print("3. Iniciar aplicativo")
        print("4. Permissões do aplicativo")
        print("5. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Implemente as funções correspondentes a cada opção do menu

    def MenuRepository(self):
        self.refresh.Fresh()
        print("\nMenu de Repositórios:")
        print("1. Listar repositórios (e seus pacotes)")
        print("2. Pacotes existentes")
        print("3. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Implemente as funções correspondentes a cada opção do menu

    def MenuInfo(self):
        self.refresh.Fresh()
        print("\nMenu de Informações:")
        print("1. Máquina (Listar informações da máquina)")
        print("2. Servidor (Listar informações do servidor)")
        print("3. Arquitetura de Software (Listar informações da arquitetura de software)")
        print("4. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))

        while True:
            if choice == 1:
                self.machine.display_info()  
            elif choice == 2:
                self.server.display_info()  
            elif choice == 3:
                self.software_architecture.display_info()  
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
            choice = int(input("Escolha uma opção: "))
