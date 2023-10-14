import time, random

from loading import LoadingAnimation
from kernel import LinuxKernel
from architecture import SoftwareArchitecture
from package import Package
from hardware import Hardware


class LinuxOperatingSystem:
    # Classe que coordena e gerencia todas as operações do sistema.
    def __init__(self, version):
        # Inicializa o sistema operacional Linux com uma versão específica.
        self.version = version
        self.kernel = LinuxKernel("4.0")
        self.architecture = SoftwareArchitecture("Monolítica", "Descrição de Exemplo")
        self.hardware = Hardware
        self.repositories = []

    def DefaultRepo(self):
        from repository import Repository
        repo_data = [
        ("Debian Repository 1", "http://debian-repo1.com"),
        ("Debian Repository 2", "http://debian-repo2.com"),
        ("Debian Repository 3", "http://debian-repo3.com")
    ]
        for i in range(len(repo_data)):
            name, url = repo_data[i]
            repo = Repository(url, name)
            for _ in range(1):
                repo.repo_pack_list.append(Package({name}, {url},f"Package-{random.randint(1, 100)}", round(random.uniform(1.0, 12.0), 1)))
            self.repositories.append(repo)
            
    def InstallDistro(self, name, defaultRepo=None):
        print(f"Instalando distribuição {name}", end='')
        LoadingAnimation(3)
        print()
        
        if defaultRepo is None:
            defaultRepo = self.repositories

        for repository in defaultRepo:
            repository.DownloadRepo(repository.reponame)

    def StartSystem(self):
        print("Ligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.InitializeKernel()
        print("Sistema Linux ligado.")
        time.sleep(2)

    def ShutdownSystem(self):
        print("Desligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.ShutdownKernel()
        print("Sistema Linux desligado.")
        time.sleep(2)

