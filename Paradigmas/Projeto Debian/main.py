from loading import *
from menus import *
from list import *

# Existem TODOs pelo código. Abra os arquivos e vá encontrando-os :)

class Output:
    def __init__(self):
        self.lists = List()
        self.refresh = Refresh()
        self.linuxOS = LinuxOperatingSystem("Debian 12")
        self.server = Server("Web Server", "192.168.1.1")
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.software_architecture = SoftwareArchitecture("Monolithic", "Descrição")
        self.kernel_api = LinuxKernelAPI()

    def Run(self):
         
        self.refresh.Fresh()

        # self.linuxOS.DefaultRepo()
        # defaultRepo =  [self.linuxOS.repositories[0], self.linuxOS.repositories[1]]
        # self.linuxOS.InstallDistro("Debian", defaultRepo)
        
        # self.linuxOS.StartSystem()

        # self.kernel_api.InteractWithKernel()

        # self.server.InitializeServer()
        # self.server.AddMachine(self.machine)
        

        #Inicialização dos menus
        while True:
            choice = MainMenu().DisplayMenu()
            if choice == 1:
                HardwareMenu().DisplayMenu()
            elif choice == 2:
                AppMenu().DisplayMenu()
            elif choice == 3:
                RepositoryMenu(self.linuxOS).DisplayMenu()
            elif choice == 4:
                if InfoMenu(self.machine, self.server, self.software_architecture).DisplayMenu():
                    continue
            elif choice == 5:
                self.refresh.Fresh()
                self.linuxOS.ShutdownSystem()
                break

if __name__ == "__main__":
    Output().Run()
