from refresh import Refresh
from hardware import Hardware
from server import Server
from architecture import SoftwareArchitecture


class List:
    def __init__(self):
        self.refresh = Refresh()

    def HardwareInfo(self, hardware):
        self.refresh.Fresh()
        self.hardware = hardware

        # Obtém informações sobre a máquina e imprime
        print("Informações da Máquina:")
        print(f"Tipo: {self.hardware.machine_type}")
        print(f"Descrição: {self.hardware.description}")
        print(f"CPU: {self.hardware.cpu}")
        print(f"Memória: {self.hardware.memory}")
        print(f"Armazenamento: {self.hardware.storage}")
        if input("\nPressione Enter para voltar ao menu...") == '':
            return

    def ServerInfo(self, server):
        self.refresh.Fresh()
        self.server = server

        # Obtém informações sobre o servidor e imprime
        print("Informações do servidor:")
        print(f"Tipo: {self.server.server_type}")
        print(f"Endereço IP: {self.server.ip_address}")
        print("Máquinas conectadas:")
        for machine in self.server.machines:
            print(f"- {machine.machine_type}: {machine.description}")
        if input("\nPressione Enter para voltar ao menu...") == '':
            return

    def ArchitectureInfo(self, architecture):
        self.refresh.Fresh()
        self.architecture = architecture

        print(self.architecture.components)
        print(self.architecture.integrations)
        # Obtém informações sobre a arquitetura de software e imprime
        print("Informações da Arquitetura de Software:")
        print(f"Tipo: {self.architecture.software_type}")
        print(f"Descrição: {self.architecture.description}")
        print("Componentes:")
        for component in self.architecture.components:
            print(f"- {component}")
        print("Integrações:")
        for integration in self.architecture.integrations:
            print(f"- {integration}")
        if input("\nPressione Enter para voltar ao menu...") == '':
            return
        
    def InstalledApps(self, installed_apps):
        self.refresh.Fresh()
        self.installed_apps = installed_apps
        
        for index, app in enumerate(self.installed_apps):
            print(f"{index + 1}. {app.name} (Versão: {app.version}, {'Em execução' if app.running else 'Parado'})")
