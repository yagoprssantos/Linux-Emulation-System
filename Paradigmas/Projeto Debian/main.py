from loading import *
from menus import *
from list import *

# Existem TODOs pelo código. Abra os arquivos e vá encontrando-os :)

class Output:
    def __init__(self):
        self.refresh = Refresh()
        self.lists = List()

        self.hardware = Hardware()
        self.architecture = SoftwareArchitecture()
        self.server = Server()
        self.app_interface = ApplicationInterface()

        self.linuxOS = LinuxOperatingSystem()
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.kernel_api = LinuxKernelAPI()

    def Run(self):
         
        self.refresh.Fresh()

        # self.linuxOS.DefaultRepo()
        # defaultRepo =  [self.linuxOS.repositories[0], self.linuxOS.repositories[1]]
        # self.linuxOS.InstallDistro("Debian", defaultRepo)
        
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
