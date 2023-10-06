import time
from loading import Loading_animation
from kernelLinux import LinuxKernel
from hardware import SoftwareArchitecture

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

