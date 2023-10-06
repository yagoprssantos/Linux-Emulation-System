import os
from loading import *
from kernelLinux import *
from hardware import *
from application import *
from repository import *
from server import *
from linux import *


class Lists:

    def list_machine_info(self, machine):
        os.system('clear')
        # Obtém informações sobre a máquina e imprime
        print("Informações da Máquina:")
        print(f"Tipo: {machine.machine_type}")
        print(f"Descrição: {machine.description}")
        print(f"CPU: {machine.system_hardware.cpu}")
        print(f"Memória: {machine.system_hardware.memory}")
        print(f"Armazenamento: {machine.system_hardware.storage}")
        input("Pressione Enter para voltar ao menu...")
        ComputerController.menu_info()

    def list_server_info(self, server):
        os.system('clear')
        # Obtém informações sobre o servidor e imprime
        print("Informações do servidor:")
        print(f"Tipo: {server.server_type}")
        print(f"Endereço IP: {server.ip_address}")
        print("Máquinas conectadas:")
        for machine in server.machines:
            print(f"- {machine.machine_type}: {machine.description}")
        input("Pressione Enter para voltar ao menu...")

    def list_software_architecture_info(self, software_architecture):
        os.system('clear')
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
        ComputerController.menu_info()

class ComputerController:
    def __init__(self):
        # Criação dos repositórios e pacotes padrão
        self.create_default_repositories()
        self.lists = Lists()
        self.linux_system = LinuxOperatingSystem("Debian 12")
        self.server = Server("Web Server", "192.168.1.1")
        self.server_machine = Machine("Physical", "Dell Server")
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.software_architecture = SoftwareArchitecture("Monolithic", "Descrição")


    def run(self):
        os.system('clear')
        # Inicialização do Sistema Operacional Linux
        self.linux_system.install_distro("Debian")
        self.linux_system.start_system()

        # Criação e inicialização do Servidor + Máquina
        self.server.add_machine(self.server_machine)
        self.server.initialize()

        # Identificação da máquina
        # Interação com o Kernel do Linux
        kernel_api = LinuxKernelAPI()
        kernel_api.interact_with_kernel()

        # Inicialização dos menus
        while True:
            choice = self.menu_principal()
            if choice == 1:
                self.menu_hardware()
            elif choice == 2:
                self.menu_app()
            elif choice == 3:
                self.menu_repo()
            elif choice == 4:
                self.menu_info()
            elif choice == 5:
                os.system('clear')
                self.linux_system.shutdown_system()
                break

    def menu_principal(self):
        os.system('clear')
        print("\nMenu Principal:")
        print("1. Analisar Hardware")
        print("2. Aplicativos")
        print("3. Repositórios")
        print("4. Informações")
        print("5. Sair do Linux")
        return int(input("Escolha uma opção: "))

    def menu_hardware(self):
        os.system('clear')
        print("\nMenu de Hardware:")
        print("1. Analisar Saúde")
        print("2. Uso da CPU")
        print("3. Memória")
        print("4. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Faltou implementar as funções

    def menu_app(self):
        os.system('clear')
        print("\nMenu de Aplicativos:")
        print("1. Listar aplicativos instalados")
        print("2. Instalar aplicativos")
        print("3. Iniciar aplicativo")
        print("4. Permissões do aplicativo")
        print("5. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Faltou implementar as funções

    def menu_repo(self):
        os.system('clear')
        print("\nMenu de Repositórios:")
        print("1. Listar repositórios (e seus pacotes)")
        print("2. Pacotes existentes")
        print("3. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))
        # Faltou implementar as funções

    def menu_info(self):
        os.system('clear')
        print("\nMenu de Informações:")
        print("1. Máquina (Listar informações da máquina)")
        print("2. Servidor (Listar informações do servidor)")
        print("3. Arquitetura de Software (Listar informações da arquitetura de software)")
        print("4. Voltar para menu principal")
        choice = int(input("Escolha uma opção: "))

        while self.menu_info:
            if choice == 1:
                self.lists.list_machine_info(self.machine)
            elif choice == 2:
                self.lists.list_server_info(self.server)
            elif choice == 3:
                self.lists.list_software_architecture_info(self.software_architecture)
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
            choice = int(input("Escolha uma opção: "))  


    def create_default_repositories(self):
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
    ComputerController().run()
