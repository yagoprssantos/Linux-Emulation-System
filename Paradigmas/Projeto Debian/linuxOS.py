import random

from loading import LoadingAnimation
from kernel import LinuxKernel
from architecture import SoftwareArchitecture
from package import Package
from hardware import Hardware


class LinuxOperatingSystem:
    # Classe que coordena e gerencia todas as operações do sistema.
    def __init__(self, version="Debian 12"):
        # Inicializa o sistema operacional Linux com uma versão específica.
        self.version = version
        self.kernel = LinuxKernel("4.0")
        self.architecture = SoftwareArchitecture()
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
            repo_name, repo_url = repo_data[i]
            repo = Repository(repo_name, repo_url)
            for _ in range(5):
                pack_name = f"Package-{random.randint(1, 100)}"
                pack_version = round(random.uniform(1.0, 12.0), 1)
                repo.repo_pack_list.append(Package(repo_name, repo_url, pack_name, pack_version))
            self.repositories.append(repo)
            
    def InstallDistro(self, name, defaultRepo=None):
        print(f"Instalando distribuição {name}", end='')
        LoadingAnimation(1)
        print()
        
        if defaultRepo is None:
            defaultRepo = self.repositories

        for repository in defaultRepo:
            repository.DownloadRepo()

    def StartSystem(self):
        print("Ligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.InitializeKernel()
        print("Sistema Linux ligado.")
        

    def ShutdownSystem(self):
        print("Desligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.ShutdownKernel()
        print("Sistema Linux desligado.")
        

