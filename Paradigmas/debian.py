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
        
        # Simula a alocação e liberação de memória para um processo fictício
        allocated_memory = random.randint(1, 16)  # em GB
        print(f"Alocando {allocated_memory}GB de memória para um processo fictício.")
        Loading_animation(2)
        time.sleep(1)
        
        print(f"Liberando {allocated_memory}GB de memória após o término do processo.")
        Loading_animation(1)
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

    def get_name(self):
        # Retorna o nome do aplicativo.
        return self.name


class ApplicationInterface:
    # Classe que gerencia a execução e permissões de aplicativos.
    def __init__(self):
        # Inicializa a interface do aplicativo.
        self.applications_list = []

    def add_application(self, application):
        # Adiciona um aplicativo à lista de aplicativos disponíveis.
        self.applications_list.append(application)

    def start_application(self):
        # Pergunta ao usuário qual aplicativo ele deseja abrir.
        while True:
            print("Aplicativos disponíveis:")
            for app in self.applications_list:
                print(app.get_name())

            app_name = input("Digite o nome do aplicativo que deseja abrir: ")

            # Verifica se o aplicativo existe na lista de aplicativos.
            selected_app = None
            for app in self.applications_list:
                if app.get_name().lower() == app_name.lower():
                    selected_app = app
                    break

            if selected_app:
                LinuxKernelAPI.interact_with_kernel()
                selected_app.execute()
                print(f"{selected_app.name} iniciado e pronto para uso.")
                break
            else:
                print(f"O aplicativo '{app_name}' não foi encontrado. Por favor, tente novamente.")
                continue

    def manage_permissions(self):
        # Pergunta ao usuário qual aplicativo ele deseja gerenciar permissões.
        while True:
            print("Aplicativos disponíveis:")
            for app in self.applications_list:
                print(app.get_name())

            app_name = input("Digite o nome do aplicativo para gerenciar permissões: ")

            # Verifica se o aplicativo existe na lista de aplicativos.
            selected_app = None
            for app in self.applications_list:
                if app.get_name().lower() == app_name.lower():
                    selected_app = app
                    break

            if selected_app:
                print(f"Gerenciando permissões para {selected_app.name}", end='')
                Loading_animation(1)
                time.sleep(1) 
                permissions = ["Leitura", "Escrita", "Execução"]
                print(f"Permissões disponíveis: {', '.join(permissions)}")
                time.sleep(1)
                break
            else:
                print(f"O aplicativo '{app_name}' não foi encontrado. Por favor, tente novamente.")
                continue


class SoftwareArchitecture:
    # Classe que define a estrutura e integrações dos componentes de software.
    def __init__(self, software_type, description):
        # Inicializa a arquitetura de software com um tipo específico e descrição.
        self.software_type = software_type
        self.description = description
        self.components = []
        self.integrations = []

    def define_components(self):
        # Define os componentes de software.
        print("Definindo componentes de software", end='')
        Loading_animation(1)
        # Adicionando componentes fictícios à lista
        self.components.append("Módulo de Autenticação")
        self.components.append("Serviço de Banco de Dados")
        self.components.append("Biblioteca de Criptografia")
        print("Componentes definidos:")
        for component in self.components:
            print(f"- {component}")
        time.sleep(1)

    def define_integrations(self):
        # Define integrações de software.
        print("Definindo integrações de software", end='')
        Loading_animation(1)
        # Adicionando integrações fictícias à lista
        self.integrations.append("API REST para Comunicação entre Módulos")
        self.integrations.append("Barramento de Serviço para Integração de Aplicações")
        self.integrations.append("Middleware de Mensageria para Troca de Mensagens")
        print("Integrações definidas:")
        for integration in self.integrations:
            print(f"- {integration}")
        time.sleep(1)


class Repository:
    # Classe que armazena e gerencia pacotes de software.
    def __init__(self, address, name):
        # Inicializa o repositório com um endereço e nome específicos.
        self.address = address
        self.name = name
        self.repo_pack_list = []

    def download(self):
        # Baixa pacotes do repositório.
        print(f"Baixando pacotes de {self.address}", end='')
        Loading_animation(1)
        time.sleep(3)
        print("Pacotes baixados.")

    def list_packages(self):
        # Lista os pacotes disponíveis no repositório.
        print(f"Pacotes no repositório {self.name}:")
        for package in self.repo_pack_list:
            print(f"- {package.name} (Versão {package.version})")

    def install_package(self, package_name):
        # Instala um pacote pelo nome, se existir no repositório.
        package = next((p for p in self.repo_pack_list if p.name == package_name), None)
        if package:
            package.install()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.name}.")

    def uninstall_package(self, package_name):
        # Desinstala um pacote pelo nome, se existir e estiver instalado.
        package = next((p for p in self.repo_pack_list if p.name == package_name), None)
        if package:
            package.uninstall()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.name}.")

class Package:
    # Classe que representa um pacote de software instalável.
    def __init__(self, name, version):
        # Inicializa um pacote de software com um nome e versão.
        self.name = name
        self.version = version
        self.installed = False  # Estado de instalação

    def install(self):
        # Instala o pacote de software.
        if not self.installed:
            print(f"Instalando {self.name}; Versão {self.version}", end='')
            Loading_animation(1)
            time.sleep(2)
            self.installed = True
            print(f"Pacote '{self.name}' instalado.")
        else:
            print(f"Pacote '{self.name}' já está instalado.")

    def uninstall(self):
        # Desinstala o pacote de software.
        if self.installed:
            print(f"Desinstalando {self.name}; Versão {self.version}", end='')
            Loading_animation(1)
            time.sleep(2)
            self.installed = False
            print(f"Pacote '{self.name}' desinstalado.")
        else:
            print(f"Pacote '{self.name}' não está instalado.")


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
        self.system_hardware = Hardware("Intel i7", "16GB", "1TB SSD")



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


class ComputerController:
    def __init__(self):
        # Complete
        pass

    def run(self):
        # Complete
        pass

    def create_default_repositories():

        # Cria por padrão 3 repositórios com pacotes fictícios.
        debian_repo1 = Repository("http://debian-repo1.com", "Debian Repository 1")
        debian_repo2 = Repository("http://debian-repo2.com", "Debian Repository 2")
        debian_repo3 = Repository("http://debian-repo3.com", "Debian Repository 3")

        # Gera pacotes fictícios e os adiciona aos repositórios
        for _ in range(5):
            debian_repo1.repo_pack_list.append(Package(f"Package-{random.randint(1, 100)}", "1.0"))
            debian_repo2.repo_pack_list.append(Package(f"Package-{random.randint(101, 200)}", "2.0"))
            debian_repo3.repo_pack_list.append(Package(f"Package-{random.randint(201, 300)}", "3.0"))


if __name__ == "__main__":
    ComputerController().run()



