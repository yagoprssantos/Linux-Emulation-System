import os
from appInterface import *
from linuxOS import *
from machine import *
from list import List
from refresh import *
from server import *
from repository import Repository

"""
TODO: ARRUMAR MENU APPMENU
TODO: TERMINAR MENUS
"""

class MainMenu:
    def __init__(self):
        self.refresh = Refresh()

    def DisplayMenu(self):
        self.refresh.Fresh()
        print("\nMenu Principal:")
        print("1. Analisar Hardware")
        print("2. Aplicativos")
        print("3. Repositórios")
        print("4. Informações")
        print("5. Sair do Linux")
        return int(input("Escolha uma opção: "))

class HardwareMenu:
    def __init__(self):
        self.refresh = Refresh()

    def DisplayMenu(self):
        self.refresh.Fresh()
        print("\nMenu de Hardware:")
        print("1. Analisar Saúde")
        print("2. Uso da CPU")
        print("3. Memória")
        print("4. Voltar para menu principal")
        return int(input("Escolha uma opção: "))

class AppMenu:
    def __init__(self):
        self.refresh = Refresh()
        self.app_interface = ApplicationInterface()
        self.list = List()


    def DisplayMenu(self):
        self.refresh.Fresh()
        print("\nMenu de Aplicativos:")
        print("1. Listar aplicativos instalados")
        print("2. Instalar aplicativos")
        print("3. Iniciar aplicativo")
        print("4. Permissões do aplicativo")
        print("5. Voltar para menu principal")
        choice = input("Escolha uma opção: ")

        while True:
            if choice == "1":
                self.list.InstalledApps()
            elif choice == "2":
                app_name = input("Digite o nome do aplicativo a ser instalado: ")
                app_version = input("Digite a versão do aplicativo: ")
                self.app_interface.AddApplication(app_name, app_version)
                if input("Deseja adicionar outro aplicativo? (S/N) ") == "S":
                    return
            elif choice == "3":
                app_index = int(input("Digite o índice do aplicativo a ser iniciado: "))
                self.app_interface.StartApplication(app_index)
            elif choice == "4":
                app_index = int(input("Digite o índice do aplicativo para gerenciar permissões: "))
                self.app_interface.ManagePermissions(app_index)
            elif choice == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")


class RepositoryMenu:
    def __init__(self, repositories=[]):
        self.refresh = Refresh()
        self.repositories = repositories
        self.repository = Repository()
        

    def DisplayMenu(self):
        self.refresh.Fresh()
        print("\nMenu de Repositórios:")
        print("1. Listar todos os repositórios e seus pacotes")
        print("2. Configurar pacotes")
        print("3. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))

        while True:
            if choice == 1:
                self.repository.ListRepositories()
            elif choice == 2:
                pass
            elif choice == 3:
                break  
            else:
                print("Opção inválida. Tente novamente.")
            choice = int(input("Escolha uma opção: "))

class InfoMenu:
    def __init__(self, machine, server, software_architecture):
        self.refresh = Refresh()
        self.list = List()
        self.machine = machine
        self.server = server
        self.software_architecture = software_architecture

    def DisplayMenu(self):
        while True:
            self.refresh.Fresh()
            print("\nMenu de Informações:")
            print("1. Máquina")
            print("2. Servidor")
            print("3. Arquitetura de Software")
            print("4. Voltar para menu principal")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.list.MachineInfo(self.machine)
            elif choice == 2:
                self.list.ServerInfo(self.server)
            elif choice == 3:
                self.list.ArchitectureInfo(self.software_architecture)
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")

class MemoryMenu:
    def __init__(self):
        self.hardware = Hardware()

    def DisplayMenu(self):
        while True:
            print("\nMenu de Gerenciamento de Memória:")
            print("1. Alocar memória")
            print("2. Liberar memória")
            print("3. Voltar ao menu de hardware")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                app_name = input("Digite o nome do aplicativo para alocar memória: ")
                self.hardware.AllocateMemory(app_name)
            elif choice == "2":
                app_name = input("Digite o nome do aplicativo para liberar memória: ")
                self.hardware.ReleaseMemory(app_name)
            elif choice == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")