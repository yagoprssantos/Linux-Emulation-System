from refresh import Refresh
from appInterface import ApplicationInterface

# TODO: Analisar se todas as listas estão sendo usadas e funcionam corretamente

class List:
    def __init__(self):
        self.refresh = Refresh()
        self.apps = ApplicationInterface()

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
        
    def InstalledApps(self, installed_apps):
        self.refresh.Fresh()
        if installed_apps:
            for index, app in enumerate(installed_apps):
                print(f"{index + 1}. {app.name} (Versão: {app.version}, {'Em execução' if app.running else 'Parado'})")
        else:
            print("Nenhum aplicativo instalado.")