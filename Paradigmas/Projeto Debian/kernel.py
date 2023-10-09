import time
from loading import LoadingAnimation

# TODO: Implementar lista de dispositivos controlados

class LinuxKernel:
    # Classe que representa o Kernel do Linux responsável pelo gerenciamento de hardware, recursos do sistema e interação com dispositivos.
    def __init__(self, version):
        # Inicializa o Kernel do Linux com uma versão específica.
        self.version = version
        self.devices = []

    def InitializeKernel(self):
        # Inicializa o Kernel do Linux.
        print("Inicializando o Kernel Linux", end='')
        LoadingAnimation(1)
        print(f"Kernel Linux {self.version} inicializado com sucesso.")
        time.sleep(2)

    def ShutdownKernel(self):
        # Desliga o Kernel do Linux.
        print("Desligando o Kernel Linux", end='')
        LoadingAnimation(1)
        print(f"Kernel Linux {self.version} desligado.")
        time.sleep(2)


class LinuxKernelAPI:
    # Classe que fornece uma interface estável para os programas interagirem com o Kernel do Linux.
    def InteractWithKernel(self): 
        print("Interagindo com o Kernel do Linux", end='')
        LoadingAnimation(1)
        time.sleep(1)
