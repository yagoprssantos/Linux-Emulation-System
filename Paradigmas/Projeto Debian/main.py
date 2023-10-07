import os
from appInterface import *
from application import *
from architecture import *
from hardware import *
from kernel import *
from linuxOS import *
from loading import *
from machine import *
from menu import *
from package import *
from refresh import *
from repository import *
from server import *

"""
#!Obrigatórios
TODO 1: Consertar Repository e Package (conflito de funções) 

TODO 2: Consertar todos os menus (funcionais)

TODO 3: Adaptar main para rodar o código (atualizar self)

TODO FINAL: Conferir se usou tudo que ele pediu para usar (herança, polimorfismo, encapsulamento)

#?Bônus para melhor nota
TODO 1: Retirar todos os IFs

TODO 2: Retirar todos os GET e SET

Notas:
- 
"""

class List:

    def MachineInfo(self, machine):
        Refresh.Fresh()
        # Obtém informações sobre a máquina e imprime
        print("Informações da Máquina:")
        print(f"Tipo: {machine.machine_type}")
        print(f"Descrição: {machine.description}")
        print(f"CPU: {machine.system_hardware.cpu}")
        print(f"Memória: {machine.system_hardware.memory}")
        print(f"Armazenamento: {machine.system_hardware.storage}")
        input("Pressione Enter para voltar ao menu...")
        ComputerController.MenuInfo()

    def ServerInfo(self, server):
        Refresh.Fresh()
        # Obtém informações sobre o servidor e imprime
        print("Informações do servidor:")
        print(f"Tipo: {server.server_type}")
        print(f"Endereço IP: {server.ip_address}")
        print("Máquinas conectadas:")
        for machine in server.machines:
            print(f"- {machine.machine_type}: {machine.description}")
        input("Pressione Enter para voltar ao menu...")

    def ArchitectureInfo(self, software_architecture):
        Refresh.Fresh()
        # Obtém informações sobre a arquitetura de software e imprime
        print("Informações da Arquitetura de Software:")
        print(f"Tipo: {software_architecture.software_type}")
        print(f"Descrição: {software_architecture.description}")
        print("Componentes:")
        for component in software_architecture.components:
            print(f"- {component}")
        print("Integrações:")
        for integration in software_architecture.integrations:
            print(f"- {integration}")
        input("Pressione Enter para voltar ao menu...")
        ComputerController.MenuInfo()

class ComputerController:
    def __init__(self):
        # Criação dos repositórios e pacotes padrão
        self.CreateRepo()
        self.lists = List()
        self.linuxOS = LinuxOperatingSystem("Debian 12")
        self.server = Server("Web Server", "192.168.1.1")
        self.server_machine = Machine("Physical", "Dell Server")
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.software_architecture = SoftwareArchitecture("Monolithic", "Descrição")
        self.kernel_api = LinuxKernelAPI()
        self.menu = Menu

    def Run(self):
        Refresh.Fresh()

        self.linuxOS.InstallDistro("Debian")
        self.linuxOS.StartSystem()

        self.server.AddMachine(self.server_machine)
        self.server.InitializeServer()

        self.kernel_api.InteractWithKernel()

        # Inicialização dos menus
        while True:
            choice = self.menu.MenuPrincipal()
            if choice == 1:
                self.menu.MenuHardware()
            elif choice == 2:
                self.menu.MenuApp()
            elif choice == 3:
                self.menu.MenuRepository()
            elif choice == 4:
                self.menu.MenuInfo()
            elif choice == 5:
                Refresh.Fresh()
                self.linuxOS.ShutdownSystem()
                break

    def CreateRepo(self):
        # Criação dos repositórios padrão com pacotes fictícios
        debian_repo1 = Repository("http://debian-repo1.com", "Debian Repository 1")
        debian_repo2 = Repository("http://debian-repo2.com", "Debian Repository 2")
        debian_repo3 = Repository("http://debian-repo3.com", "Debian Repository 3")

        # Geração de pacotes fictícios e adição aos repositórios
        for _ in range(3):
            debian_repo1.repo_pack_list.append(Package(f"Package-{random.randint(1, 100)}", "1.0"))
            debian_repo2.repo_pack_list.append(Package(f"Package-{random.randint(101, 200)}", "2.0"))
            debian_repo3.repo_pack_list.append(Package(f"Package-{random.randint(201, 300)}", "3.0"))


if __name__ == "__main__":
    ComputerController().Run()
