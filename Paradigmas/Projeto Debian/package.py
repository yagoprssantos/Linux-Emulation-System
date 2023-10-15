import random

from loading import LoadingAnimation
from repository import Repository


class Package(Repository):
    # Classe que representa um pacote de software instalável.
    def __init__(self, reponame, address, packname, version):
        super().__init__(reponame, address)
        self.reponame = reponame
        self.packname = packname
        self.version = version
        self.installed = False

    def install(self):
        # Instala o pacote de software
        if not self.installed:
            print(f"Instalando {self.packname} (Versão: {self.version}) do repositório {self.reponame}", end='')
            LoadingAnimation(1)
            self.installed = True
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} instalado.\n")
        else:
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} já está instalado.\n")

    def uninstall(self):
        # Desinstala o pacote de software
        if self.installed:
            print(f"Desinstalando {self.packname} (Versão: {self.version}) do repositório {self.reponame}", end='')
            LoadingAnimation(1)
            
            self.installed = False
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} desinstalado.")
        else:
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} não está instalado.")

