from loading import LoadingAnimation


class Repository:
    # Classe que armazena informações e funções de repositórios
    def __init__(self, reponame, address):
        self.reponame = reponame
        self.address = address
        self.repo_pack_list = []

    def DownloadRepo(self):
        print(f"Endereço: {self.address}\nBaixando pacotes do repositório {self.reponame}", end='')
        LoadingAnimation(1)
        print("\n")
        # Faz loop para baixar todos os pacotes do repositório
        for package in self.repo_pack_list:
            package.install()
        print(f"Pacotes do repositório {self.reponame} baixados.\n")

    def ListPackages(self):
        print(f"\nPacotes no repositório {self.reponame}:")
        for package in self.repo_pack_list:
            print(f"- {package.packname} // Versão: {package.version} // Instalado: {package.installed}")

    def InstallPackage(self, package_name):
        # Instala um pacote pelo nome, se existir no repositório
        package = next((p for p in self.repo_pack_list if p.packname == package_name), None)
        if package:
            package.install()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.reponame}.")

    def UninstallPackage(self, package_name):
        # Desinstala um pacote pelo nome, se existir e estiver instalado
        package = next((p for p in self.repo_pack_list if p.packname == package_name), None)
        if package:
            package.uninstall()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.reponame}.")
