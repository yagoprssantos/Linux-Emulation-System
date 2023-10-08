import time
from loading import LoadingAnimation
from package import Package

class Repository:
    # Classe que armazena e gerencia pacotes de software.
    def __init__(self, address, name):
        # Inicializa o repositório com um endereço e nome específicos.
        self.address = address
        self.name = name
        self.repo_pack_list = []

    def DownloadRepo(self, name):
        # Baixa pacotes do repositório.
        print(f"Endereço: {self.address}\nBaixando pacotes do repositório {self.name}", end='')
        LoadingAnimation(1)
        time.sleep(1)

        # Faz loop para baixar todos os pacotes do repositório
        for package in self.repo_pack_list:
            package.install()

        print(f"Pacotes do repositório {self.name} baixados.\n")

    def ListPackages(self):
        # Lista os pacotes disponíveis no repositório.
        print(f"Pacotes no repositório {self.name}:")
        for package in self.repo_pack_list:
            print(f"- Nome: {package.name}")
            print(f"  Versão: {package.version}")
            print(f"  Instalado: {'Sim' if package.installed else 'Não'}\n")

    def InstallPackage(self, package_name):
        # Instala um pacote pelo nome, se existir no repositório.
        package = next((p for p in self.repo_pack_list if p.name == package_name), None)
        if package:
            package.install(package)
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.name}.")

    def UninstallPackage(self, package_name):
        # Desinstala um pacote pelo nome, se existir e estiver instalado.
        package = next((p for p in self.repo_pack_list if p.name == package_name), None)
        if package:
            package.uninstall(package)
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.name}.")

    def ListRepositories(self):
        for package in self.repo_pack_list:
            print(f"- Nome: {package.name}")
            print(f"  Versão: {package.version}")
            print(f"  Instalado: {'Sim' if package.installed else 'Não'}")