import time
from loading import LoadingAnimation

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
            LoadingAnimation(1)
            self.installed = True
            print(f"Pacote '{self.name}' instalado.\n")
        else:
            print(f"Pacote '{self.name}' já está instalado.\n")

    def uninstall(self):
        # Desinstala o pacote de software.
        if self.installed:
            print(f"Desinstalando {self.name}; Versão {self.version}", end='')
            LoadingAnimation(1)
            time.sleep(2)
            self.installed = False
            print(f"Pacote '{self.name}' desinstalado.")
        else:
            print(f"Pacote '{self.name}' não está instalado.")

