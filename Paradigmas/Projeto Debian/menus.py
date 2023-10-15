import os

from appInterface import *
from linuxOS import *
from machine import *
from list import List
from refresh import *
from server import *
from repository import Repository

# TODO: Terminar menus:
#!           - HardwareMenu   (Não foi feito)
#?           - AppMenu        (Incompleto)
#*           - RepositoryMenu (Completo)
#*           - InfoMenu       (Completo)
#            - MemoryMenu     (Em testes)


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
 

class AppMenu:
    def __init__(self):
        self.refresh = Refresh()
        self.app_interface = ApplicationInterface()
        self.list = List()

    def DisplayMenu(self):
        while True:
            self.refresh.Fresh()
            print("\nMenu de Aplicativos:")
            print("1. Listar aplicativos instalados")
            print("2. Configurar aplicativos")
            print("3. Voltar para menu principal")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.list.InstalledApps(self.app_interface.installed_apps)
                input("\nPressione Enter para voltar ao menu...")
            elif choice == "2":
                ConfigAppMenu().DisplayMenu()
            elif choice == "3":
                break

            else:
                print("Opção inválida. Tente novamente.")

class ConfigAppMenu:
    def __init__(self):
        self.refresh = Refresh()
        self.app_interface = ApplicationInterface()
        self.list = List()

    def DisplayMenu(self):
        while True:
            self.refresh.Fresh()
            print("\nConfigurações de Aplicativos:")
            print("1. Instalar aplicativos")
            print("2. Desinstalar aplicativo")
            print("3. Iniciar aplicativo")
            print("4. Parar aplicativo")
            print("5. Permissões do aplicativo")
            print("6. Voltar para menu de aplicativos")
            choice = input("Escolha uma opção: ")
            
            if choice == "1":
                self.refresh.Fresh()
                while True:
                    app_name = str(input("\nDigite o nome do aplicativo a ser instalado: "))
                    app_version = round(float(input("Digite a versão do aplicativo (float): ")), 1)
                    self.app_interface.AddApplication(app_name, app_version)
                    if input("Deseja adicionar outro aplicativo? (S/N) ").upper() == "N":
                        break  
            elif choice == "2":
                self.list.InstalledApps(self.app_interface.installed_apps)
                index = int(input("\nDigite o índice do aplicativo a ser desinstalado: ")) - 1
                self.app_interface.RemoveApplication(index)
                input("\nPressione Enter para voltar ao menu...")

            elif choice == "3":
                self.list.InstalledApps(self.app_interface.installed_apps)
                index = int(input("\nDigite o índice do aplicativo a ser iniciado: ")) - 1
                self.app_interface.StartApplication(index)
                input("\nPressione Enter para voltar ao menu...")

            elif choice == "4":
                self.list.InstalledApps(self.app_interface.installed_apps)
                index = int(input("\nDigite o índice do aplicativo a ser parado: ")) - 1
                self.app_interface.StopApplication(index)
                input("\nPressione Enter para voltar ao menu...")

            elif choice == "5":
                self.list.InstalledApps(self.app_interface.installed_apps)
                index = int(input("\nDigite o índice do aplicativo para gerenciar permissões: ")) - 1
                self.app_interface.ManagePermissions(index)

            elif choice == "6":
                break

            else:
                print("Opção inválida. Tente novamente.")

class RepositoryMenu:
    def __init__(self, linuxOS):
        self.refresh = Refresh()
        self.repositories = linuxOS.repositories

    def DisplayMenu(self):
        while True:
            self.refresh.Fresh()
            print("\nMenu de Repositórios:")
            print("1. Listar todos os repositórios e seus pacotes")
            print("2. Configurar pacotes")
            print("3. Voltar para menu principal")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.refresh.Fresh() 
                for reponame in self.repositories:
                    reponame.ListPackages()
                input("Pressione Enter para voltar ao menu...")
            elif choice == 2:
                self.refresh.Fresh()
                print("\nMenu de Repositórios:")
                for i, repo in enumerate(self.repositories, start=1):
                    print(f"{i}. {repo.reponame}")
                print(f"{i+1}. Voltar para menu principal")
                while True:
                    choice = int(input("Escolha uma opção: "))

                    if choice == i+1:
                        break
                    elif choice in range(1, i+1):
                        repository = self.repositories[choice-1]
                        PackageMenu(repository).DisplayMenu()
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            elif choice == 3:
                break  
            else:
                print("Opção inválida. Tente novamente.")

class PackageMenu:
    def __init__(self, reponame):
        self.refresh = Refresh()
        self.reponame = reponame

    def DisplayMenu(self):
        while True:
            self.refresh.Fresh()
            print(f"\nMenu de Pacotes do repositório '{self.reponame.reponame}':")
            print("1. Listar todos os pacotes")
            print("2. Instalar pacotes")
            print("3. Desinstalar pacotes")
            print("4. Voltar para menu de repositórios")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.refresh.Fresh()
                self.reponame.ListPackages()
                input("Pressione Enter para voltar ao menu...")
                pass
            elif choice == 2:
                while True:
                    self.refresh.Fresh()
                    i = 0
                    print("Pacotes disponíveis:")
                    for package in self.reponame.repo_pack_list:
                        print(f"{i+1}. {package.packname} // Versão: {package.version} // Instalado: {package.installed}")
                        i += 1
                    print(f"{i+1}. Voltar para menu de pacotes\n")
                    choice = int(input("Escolha uma opção: "))
                    print("\n")
                    if choice == i+1:
                        break
                    elif choice in range(1, i+1):
                        self.reponame.InstallPackage(self.reponame.repo_pack_list[choice-1].packname)
                        input("\nPressione Enter para voltar ao menu...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            elif choice == 3:
                self.refresh.Fresh()
                while True:
                    i = 0
                    print("Pacotes disponíveis:")
                    for package in self.reponame.repo_pack_list:
                        print(f"{i+1}. {package.packname} // Versão: {package.version} // Instalado: {package.installed}")
                        i += 1
                    print(f"{i+1}. Voltar para menu de pacotes\n")
                    choice = int(input("Escolha uma opção: "))
                    print("\n")

                    if choice == i+1:
                        break
                    elif choice in range(1, i+1):
                        self.reponame.UninstallPackage(self.reponame.repo_pack_list[choice-1].packname)
                        input("\nPressione Enter para voltar ao menu...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            elif choice == 4:
                return
            else:
                print("Opção inválida. Tente novamente.")
            


class InfoMenu:
    def __init__(self, machine, server, software_architecture):
        self.refresh = Refresh()
        self.list = List()
        self.hardware = Hardware()
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
                self.list.HardwareInfo(self.hardware)
            elif choice == 2:
                self.list.ServerInfo(self.server)
            elif choice == 3:
                self.list.ArchitectureInfo(self.software_architecture)
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
