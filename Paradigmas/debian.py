"""
? ADICONAR INTERAÇÃO COM KERNEL

* Loading_animation
* LinuxKernel
! LinuxKernelAPI
TODO: Fazer com que o kernel seja usado todas as vezes que necessário
TODO: (acessar hardware, executar sudo, coisas que afetam diretamente o sistema)
? Hardware
* ApplicationInterface + MELHORAR PERMISSÕES
* Application
* SoftwareArchitecture
! LinuxOperatingSystem MELHORAR
? Repository
? Package
TODO: juntar Repository e Package para executarem juntos
* Server
* Machine


TODO MAIN: Fazer prints na ordem certa!
1. Instalar Linux
2. Iniciar o Linux
3. Aparecer Menu Interativo 
(DeviceController, Hardware, App,
Info(Software Architecture, Machine, Server), Sair do Linux)
4. Finalizar Linux
"""

import random
import time
import sys

# Função meramente ilustrativa para imitar o loading
def Loading_animation(repeat_times):
    for _ in range(repeat_times):
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            # Tempo entre os pontos
            time.sleep(1)

        # Clear nos pontos
        sys.stdout.write("\b\b\b   \b\b\b")  
        sys.stdout.flush()
        # Tempo para voltar o loop
        time.sleep(0.5)
    sys.stdout.write("...\n")


class LinuxKernel:
    # Classe que representa o kernel do Linux responsável pelo gerenciamento de hardware, recursos do sistema e interação com dispositivos.
    def __init__(self, version):
        # Inicializa o kernel do Linux com uma versão específica.
        self.version = version

    def initialize(self):
        # Inicializa o kernel do Linux.
        print("Inicializando o Kernel Linux", end='')
        Loading_animation(1)
        print(f"Kernel Linux {self.version} inicializado com sucesso.")
        time.sleep(2)

    def shutdown(self):
        # Desliga o kernel do Linux.
        print("Desligando o Kernel Linux", end='')
        Loading_animation(1)
        print(f"Kernel Linux {self.version} desligado.")
        time.sleep(2)


class LinuxKernelAPI:
    # Classe que fornece uma interface estável para os programas interagirem com o kernel do Linux.
    def interact_with_kernel(self): 
        print("Interagindo com o kernel do Linux", end='')
        Loading_animation(1)
        time.sleep(1)

class Hardware:
    # Classe que representa os componentes de hardware de uma máquina.
    def __init__(self, cpu, memory, storage):
        # Inicializa os componentes de hardware: CPU, memória e armazenamento.
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def check_health(self):
        # Verifica o estado de saúde dos componentes de hardware.
        print("Verificando integridade dos componentes de hardware", end='')
        Loading_animation(1)
        LinuxKernelAPI.interact_with_kernel()
        health_list = ["Péssimo", "Ruim", "Ok", "Bom", "Ótimo"] 
        print(f"Saúde do hardware: {random.choice(health_list)}!")
        time.sleep(1)

    def monitor_cpu_usage(self):
        # Monitora o uso da CPU.
        print("Monitorando o uso da CPU", end='')
        Loading_animation(1)
        LinuxKernelAPI.interact_with_kernel()
        cpu_usage = random.randint(10, 90)  # Simula o uso aleatório da CPU
        print(f"Uso da CPU: {cpu_usage}%")
        time.sleep(1)

    def manage_memory(self):
        # Gerencia os recursos de memória.
        print("Gerenciando os recursos de memória", end='')
        Loading_animation(1)
        LinuxKernelAPI.interact_with_kernel()

class ApplicationInterface:
    # Classe que gerencia a execução e permissões de aplicativos.
    def __init__(self):
        # Inicializa a interface do aplicativo.
        self.applications_list = []

    def add_application(self, application):
        # Adiciona um aplicativo à lista de aplicativos disponíveis.
        self.applications_list.append(application)

    def start_application(self, application):
        # Inicia o aplicativo especificado.
        Application.execute(application)
        time.sleep(2)
        print(f"{application.name} iniciado e pronto para uso.")

    def manage_permissions(self, application):
        # Gerencia permissões para o aplicativo especificado.
        print(f"Gerenciando permissões para {application.name}", end='')
        Loading_animation(1)
        time.sleep(1) 
        permissions = ["Leitura", "Escrita", "Execução"]
        print(f"Permissões disponíveis: {', '.join(permissions)}")
        time.sleep(1)

    
class Application:
    # Classe que representa um aplicativo instalado.
    def __init__(self, name):
        # Inicializa um aplicativo com um nome e versão.
        self.name = name
        self.version = round(random.uniform(1.0, 12.0), 1)  # Versão aleatória entre 1.0 e 12.0

    def execute(self):
        # Executa o aplicativo.
        print(f"Executando {self.name}; Versão: {self.version}", end='')
        Loading_animation(1)
        time.sleep(2)


class SoftwareArchitecture:
    # Classe que define a estrutura e integrações dos componentes de software.
    def __init__(self, software_type, description):
        # Inicializa a arquitetura de software com um tipo específico e descrição.
        self.software_type = software_type
        self.description = description
        self.components = []

    def define_components(self):
        # Define os componentes de software.
        print("Definindo componentes de software", end='')
        Loading_animation(1)
        time.sleep(1)

    def define_integrations(self):
        # Define integrações de software.
        print("Definindo integrações de software", end='')
        Loading_animation(1)
        time.sleep(1)


class LinuxOperatingSystem:
    # Classe que coordena e gerencia todas as operações do sistema.
    def __init__(self, version):
        # Inicializa o sistema operacional Linux com uma versão específica.
        self.version = version
        self.kernel = LinuxKernel("4.0")
        self.architecture = SoftwareArchitecture("Monolítica", "Descrição de Exemplo")
        self.repositories = []

    def install_distro(self, name):
        # Instala a distribuição Linux.
        # Faça uma série de prints que simule a instalação do Debian.
        print(f"Instalando distribuição {name}", end='')
        Loading_animation(3)
        for repository in self.repositories:
            repository.download()
        time.sleep(3)

    def start_system(self):
        # Inicia o sistema Linux.
        print("Ligando o Sistema Linux", end='')
        Loading_animation(1)
        self.kernel.initialize()
        print("Sistema Linux ligado.")
        time.sleep(2)


    def shutdown_system(self):
        # Desliga o sistema Linux.
        print("Desligando o Sistema Linux", end='')
        Loading_animation(1)
        self.kernel.shutdown()
        print("Sistema Linux desligado.")
        time.sleep(2)


class Repository:
    # Classe que armazena e gerencia pacotes de software.
    def __init__(self, address, name):
        # Inicializa o repositório com um endereço e nome específicos.
        self.address = address
        self.name = name
        self.packages = []

    def download(self):
        # Baixa pacotes do repositório.
        print(f"Baixando pacotes de {self.address}", end='')
        Loading_animation(1)
        time.sleep(3)
        print("Pacotes baixados.")

    def upload(self):
        # Faz upload de pacotes para o repositório.
        print(f"Enviando pacotes para {self.address}", end='')
        Loading_animation(1)
        time.sleep(1)
        print("Pacotes enviados.")


class Package:
    # Classe que representa um pacote de software instalável.
    def __init__(self, name, version):
        # Inicializa um pacote de software com um nome e versão.
        self.name = name
        self.version = version

    def install(self):
        # Instala o pacote de software.
        print(f"Instalando {self.name}; Versão {self.version}", end='')
        Loading_animation(1)
        time.sleep(2)
        print(f"Pacote '{self.name}' instalado.")


class Server:
    # Classe que fornece serviços a outras máquinas na rede.
    def __init__(self, server_type, ip_address):
        # Inicializa o servidor com um tipo e endereço IP específicos.
        self.server_type = server_type
        self.ip_address = ip_address
        self.machines = []

    def initialize(self):
        # Inicializa o servidor.
        print(f"Servidor {self.server_type} no endereço {self.ip_address} inicializado.")
        time.sleep(2)

    def shutdown(self):
        # Desliga o servidor.
        print(f"Servidor {self.server_type} no endereço {self.ip_address} desligado.")
        time.sleep(2)

    def add_machine(self, machine):
        # Adiciona uma máquina ao servidor.
        self.machines.append(machine)
        print(f"Máquina adicionada ao servidor no endereço {self.ip_address}.")
        time.sleep(2)


class Machine:
    # Classe que representa uma máquina física ou virtual.
    def __init__(self, machine_type, description):
        # Inicializa uma máquina com um tipo e descrição específicos.
        self.machine_type = machine_type
        self.description = description
        self.application_interface = ApplicationInterface()
        self.system_hardware = Hardware("Intel i7", "16GB", "1TB SSD")

    def execute_application(self, application):
        # Executa o aplicativo especificado na máquina.
        self.application_interface.start_application(application)

class ComputerController:
    def __init__(self):
        self.linux_os = LinuxOperatingSystem("Debian 12")
        self.kernel_api = LinuxKernelAPI()
        self.system_hardware = Hardware("Intel i7", "16GB", "1TB SSD")
        self.app_name = "MyApp"
        self.installed_app = Application(self.app_name)
        self.app_interface = ApplicationInterface()
        self.software_architecture = SoftwareArchitecture("Monolithic", "Description")
        self.repo_address = "http://example.com/repo"
        self.repo_name = "Main Repository"
        self.repository = Repository(self.repo_address, self.repo_name)
        self.server = Server("Web Server", "192.168.1.1")
        self.server_machine = Machine("Physical", "Dell Server")

    def run(self):
        pass

if __name__ == "__main__":
    ComputerController()



