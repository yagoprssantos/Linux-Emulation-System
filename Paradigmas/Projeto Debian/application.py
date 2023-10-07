import time, random
from loading import LoadingAnimation
from kernel import LinuxKernelAPI

class Application:
    # Classe que representa um aplicativo instalado.
    def __init__(self, name):
        # Inicializa um aplicativo com um nome e versão.
        self.name = name
        self.version = round(random.uniform(1.0, 12.0), 1)  # Versão aleatória entre 1.0 e 12.0

    def ExecuteApp(self):
        # Executa o aplicativo.
        print(f"Executando {self.name}; Versão: {self.version}", end='')
        LoadingAnimation(1)
        time.sleep(2)

    def GetName(self):
        # Retorna o nome do aplicativo.
        return self.name

