import time

from loading import LoadingAnimation

# TODO: Fazer com que o DownloadRepo utilize o reponame e salve corretamente o nome do repositório

class Repository:
    # Classe que armazena informações e funções de repositórios
    def __init__(self, reponame, address):
        self.reponame = reponame
        self.address = address
        self.repo_pack_list = []

    def DownloadRepo(self, reponame):
        print(f"Endereço: {self.address}\nBaixando pacotes do repositório {self.reponame}", end='')
        LoadingAnimation(2)
        time.sleep(1)
        # Faz loop para baixar todos os pacotes do repositório
        for package in self.repo_pack_list:
            # Use the repository name from the Package object
            package.install(package.reponame)
        print(f"Pacotes do repositório {self.reponame} baixados.\n")

    def ListPackages(self):
        print(f"Pacotes no repositório {self.reponame}:")
        for package in self.repo_pack_list:
            print(f"- Nome: {package.packname}")
            print(f"  Versão: {package.version}")
            print(f"  Instalado: {'Sim' if package.installed else 'Não'}\n")

    def InstallPackage(self, package_name):
        # Instala um pacote pelo nome, se existir no repositório
        package = next((p for p in self.repo_pack_list if p.reponame == package_name), None)
        if package:
            package.install(package)
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.reponame}.")

    def UninstallPackage(self, package_name):
        # Desinstala um pacote pelo nome, se existir e estiver instalado
        package = next((p for p in self.repo_pack_list if p.reponame == package_name), None)
        if package:
            package.uninstall(package)
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.reponame}.")