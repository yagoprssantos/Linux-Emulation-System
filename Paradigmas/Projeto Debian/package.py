import time, random

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

    def install(self, reponame):
        # Instala o pacote de software
        if not self.installed:
            print(f"Instalando {self.packname} do repositório {reponame}; Versão {self.version}", end='')
            LoadingAnimation(1)
            self.installed = True
            print(f"Pacote '{self.packname}' do repositório '{reponame}' instalado.\n")
        else:
            print(f"Pacote '{self.packname}' do repositório '{reponame}' já está instalado.\n")

    def uninstall(self, reponame):
        # Desinstala o pacote de software
        if self.installed:
            print(f"Desinstalando {self.packname} do repositório '{reponame}'; Versão {self.version}", end='')
            LoadingAnimation(1)
            time.sleep(2)
            self.installed = False
            print(f"Pacote '{self.packname}' do repositório '{reponame}' desinstalado.")
        else:
            print(f"Pacote '{self.packname}' do repositório '{reponame}' não está instalado.")

