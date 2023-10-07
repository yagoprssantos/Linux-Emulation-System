import time
from loading import LoadingAnimation
from kernel import LinuxKernel
from architecture import SoftwareArchitecture

class LinuxOperatingSystem:
    # Classe que coordena e gerencia todas as operações do sistema.
    def __init__(self, version):
        # Inicializa o sistema operacional Linux com uma versão específica.
        self.version = version
        self.kernel = LinuxKernel("4.0")
        self.architecture = SoftwareArchitecture("Monolítica", "Descrição de Exemplo")
        self.repositories = []

    def InstallDistro(self, name):
        # Instala a distribuição Linux.
        # Faça uma série de prints que simule a instalação do Debian.
        print(f"Instalando distribuição {name}", end='')
        LoadingAnimation(3)
        for repository in self.repositories:
            repository.DownloadRepo()
        time.sleep(3)

    def StartSystem(self):
        # Inicia o sistema Linux.
        print("Ligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.InitializeKernel()
        print("Sistema Linux ligado.")
        time.sleep(2)

    def ShutdownSystem(self):
        # Desliga o sistema Linux.
        print("Desligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.ShutdownKernel()
        print("Sistema Linux desligado.")
        time.sleep(2)

