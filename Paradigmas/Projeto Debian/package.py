import time, repository
from loading import LoadingAnimation

class Package(repository):
    # Classe que representa um pacote de software instalável.
    def __init__(self, address, reponame, packname, version):
        super().__init__(address, reponame)
        # Inicializa um pacote de software com um nome e versão.
        self.packname = packname
        self.version = version
        self.installed = False  # Estado de instalação

    def install(self):
        # Instala o pacote de software.
        if not self.installed:
            print(f"Instalando {self.packname}; Versão {self.version}", end='')
            LoadingAnimation(1)
            self.installed = True
            print(f"Pacote '{self.packname}' instalado.\n")
        else:
            print(f"Pacote '{self.packname}' já está instalado.\n")

    def uninstall(self):
        # Desinstala o pacote de software.
        if self.installed:
            print(f"Desinstalando {self.packname}; Versão {self.version}", end='')
            LoadingAnimation(1)
            time.sleep(2)
            self.installed = False
            print(f"Pacote '{self.packname}' desinstalado.")
        else:
            print(f"Pacote '{self.packname}' não está instalado.")

