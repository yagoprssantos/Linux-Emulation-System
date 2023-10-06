import time
from loading import Loading_animation

class Repository:
    # Classe que armazena e gerencia pacotes de software.
    def __init__(self, address, name):
        # Inicializa o repositório com um endereço e nome específicos.
        self.address = address
        self.name = name
        self.repo_pack_list = []

    def download(self):
        # Baixa pacotes do repositório.
        print(f"Baixando pacotes de {self.address}", end='')
        Loading_animation(1)
        time.sleep(3)
        print("Pacotes baixados.")

    def list_packages(self):
        # Lista os pacotes disponíveis no repositório.
        print(f"Pacotes no repositório {self.name}:")
        for package in self.repo_pack_list:
            print(f"- {package.name} (Versão {package.version})")

    def install_package(self, package_name):
        # Instala um pacote pelo nome, se existir no repositório.
        package = next((p for p in self.repo_pack_list if p.name == package_name), None)
        if package:
            package.install()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.name}.")

    def uninstall_package(self, package_name):
        # Desinstala um pacote pelo nome, se existir e estiver instalado.
        package = next((p for p in self.repo_pack_list if p.name == package_name), None)
        if package:
            package.uninstall()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.name}.")

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
            Loading_animation(1)
            time.sleep(2)
            self.installed = True
            print(f"Pacote '{self.name}' instalado.")
        else:
            print(f"Pacote '{self.name}' já está instalado.")

    def uninstall(self):
        # Desinstala o pacote de software.
        if self.installed:
            print(f"Desinstalando {self.name}; Versão {self.version}", end='')
            Loading_animation(1)
            time.sleep(2)
            self.installed = False
            print(f"Pacote '{self.name}' desinstalado.")
        else:
            print(f"Pacote '{self.name}' não está instalado.")

