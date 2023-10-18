from loading import *
from menus import *
from list import *

# Existem TODOs pelo código. Abra os arquivos e vá encontrando-os :)

class Output:
    def __init__(self):
        self.refresh = Refresh()
        self.lists = List()

        self.hardware = Hardware("Físico", "Samsung", "Intel i7", "16GB", "1TB SSD")
        self.architecture = SoftwareArchitecture("Monolítica", "Arquitetura de software monolítica")
        self.server = Server("Web Server", "192.168.1.1")
        self.app_interface = ApplicationInterface(self.hardware)
        self.kernel = LinuxKernel("5.10.0-8-amd64")

        self.linuxOS = LinuxOperatingSystem("Debian 12", self.kernel, self.architecture, self.hardware)
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.kernel_api = LinuxKernelAPI()

    def Run(self):
         
        self.refresh.Fresh()

        self.linuxOS.DefaultRepo()
        defaultRepo =  [self.linuxOS.repositories[0], self.linuxOS.repositories[1]]
        self.linuxOS.InstallDistro("Debian", defaultRepo)
        
        self.linuxOS.StartSystem()

        self.kernel_api.InteractWithKernel()

        self.architecture.DefineComponents()
        self.architecture.DefineIntegrations()
        
        self.server.InitializeServer()
        self.server.AddMachine(self.machine)
        

        #Inicialização dos menus
        while True:
            choice = MainMenu().DisplayMenu()
            if choice == 1:
                HardwareMenu(self.hardware, self.app_interface).DisplayMenu()
            elif choice == 2:
                AppMenu(self.app_interface).DisplayMenu()
            elif choice == 3:
                RepositoryMenu(self.linuxOS).DisplayMenu()
            elif choice == 4:
                if InfoMenu(self.hardware, self.server, self.architecture).DisplayMenu():
                    continue
            elif choice == 5:
                self.refresh.Fresh()
                self.linuxOS.ShutdownSystem()
                break

if __name__ == "__main__":
    Output().Run()
