import os
from appInterface import *
from application import *
from architecture import *
from hardware import *
from kernel import *
from linuxOS import *
from list import *
from loading import *
from machine import *
from menus import *
from package import *
from refresh import *
from repository import *
from server import *

"""
#!Obrigatórios
//TODO 1: Consertar Repository e Package (conflito de funções) 

TODO 2: Consertar todos os menus (funcionais)

TODO 3: Adaptar main para rodar o código (atualizar self)

TODO FINAL: Conferir se usou tudo que ele pediu para usar (herança, polimorfismo, encapsulamento)

#?Bônus para melhor nota
TODO 1: Retirar todos os IFs

TODO 2: Retirar todos os GET e SET

Notas:
- Necessário definir componentes e integrações
- Poderia tentar fazer com que o List se torne um arquivo separado
! Terá conflito entre menus e list
"""

class List:

    def __init__(self):
        self.refresh = Refresh()

    def MachineInfo(self, machine):
        self.refresh.Fresh()
        # Obtém informações sobre a máquina e imprime
        print("Informações da Máquina:")
        print(f"Tipo: {machine.machine_type}")
        print(f"Descrição: {machine.description}")
        print(f"CPU: {machine.system_hardware.cpu}")
        print(f"Memória: {machine.system_hardware.memory}")
        print(f"Armazenamento: {machine.system_hardware.storage}")
        if input("Pressione Enter para voltar ao menu...") == '':
            return

    def ServerInfo(self, server):
        self.refresh.Fresh()
        # Obtém informações sobre o servidor e imprime
        print("Informações do servidor:")
        print(f"Tipo: {server.server_type}")
        print(f"Endereço IP: {server.ip_address}")
        print("Máquinas conectadas:")
        for machine in server.machines:
            print(f"- {machine.machine_type}: {machine.description}")
        if input("Pressione Enter para voltar ao menu...") == '':
            return

    def ArchitectureInfo(self, software_architecture):
        self.refresh.Fresh()
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
        if input("Pressione Enter para voltar ao menu...") == '':
            return

class Output:
    def __init__(self):
        self.lists = List()
        self.refresh = Refresh()
        self.linuxOS = LinuxOperatingSystem("Debian 12")
        self.server = Server("Web Server", "192.168.1.1")
        self.server_machine = Machine("Physical", "Dell Server")
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.software_architecture = SoftwareArchitecture("Monolithic", "Descrição")
        self.kernel_api = LinuxKernelAPI()

    def Run(self):
                
        self.refresh.Fresh()

        self.linuxOS.DefaultRepo()
        defaultRepo =  [self.linuxOS.repositories[0], self.linuxOS.repositories[1]]
        self.linuxOS.InstallDistro("Debian", defaultRepo)
        
        self.linuxOS.StartSystem()

        self.kernel_api.InteractWithKernel()

        self.server.AddMachine(self.server_machine)
        self.server.InitializeServer()


        # Inicialização dos menus
        while True:
            choice = MainMenu().DisplayMenu()
            if choice == 1:
                HardwareMenu().DisplayMenu()
            elif choice == 2:
                AppMenu().DisplayMenu()
            elif choice == 3:
                RepositoryMenu().DisplayMenu()
            elif choice == 4:
                if InfoMenu(self.machine, self.server, self.software_architecture).DisplayMenu():
                    continue
            elif choice == 5:
                self.refresh.Fresh()
                self.linuxOS.ShutdownSystem()
                break

if __name__ == "__main__":
    Output().Run()
