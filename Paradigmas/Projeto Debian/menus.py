import os
from appInterface import *
from application import *
from architecture import *
from hardware import *
from kernel import *
from linuxOS import *
from loading import *
from machine import *
from main import List
from package import *
from refresh import *
from repository import *
from server import *

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

    def DisplayMenu(self):
        self.refresh.Fresh()
        print("\nMenu de Aplicativos:")
        print("1. Listar aplicativos instalados")
        print("2. Instalar aplicativos")
        print("3. Iniciar aplicativo")
        print("4. Permissões do aplicativo")
        print("5. Voltar para menu principal")
        return int(input("Escolha uma opção: "))

class RepositoryMenu:
    def __init__(self, repositories=[]):
        self.refresh = Refresh()
        self.repositories = repositories

    def DisplayMenu(self):
        self.refresh.Fresh()
        print("\nMenu de Repositórios:")
        print("1. Listar todos os repositórios e seus pacotes")
        print("2. Configurar pacotes")
        print("3. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))

        while True:
            if choice == 1:
                pass
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
