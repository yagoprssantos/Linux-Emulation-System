import time
from kernel import LinuxKernelAPI
from loading import LoadingAnimation

class ApplicationInterface:
    # Classe que gerencia a execução e permissões de aplicativos.
    def __init__(self):
        # Inicializa a interface do aplicativo.
        self.applications_list = []

    def AddApplication(self, application):
        # Adiciona um aplicativo à lista de aplicativos disponíveis.
        self.applications_list.append(application)

    def StartApplication(self):
        # Pergunta ao usuário qual aplicativo ele deseja abrir.
        while True:
            print("Aplicativos disponíveis:")
            for app in self.applications_list:
                print(app.GetName())

            app_name = input("Digite o nome do aplicativo que deseja abrir: ")

            # Verifica se o aplicativo existe na lista de aplicativos.
            selected_app = None
            for app in self.applications_list:
                if app.GetName().lower() == app_name.lower():
                    selected_app = app
                    break

            if selected_app:
                LinuxKernelAPI.InteractWithKernel()
                selected_app.ExecuteApp()
                print(f"{selected_app.name} iniciado e pronto para uso.")
                break
            else:
                print(f"O aplicativo '{app_name}' não foi encontrado. Por favor, tente novamente.")
                continue

    def ManagePermissions(self):
        # Pergunta ao usuário qual aplicativo ele deseja gerenciar permissões.
        while True:
            print("Aplicativos disponíveis:")
            for app in self.applications_list:
                print(app.GetName())

            app_name = input("Digite o nome do aplicativo para gerenciar permissões: ")

            # Verifica se o aplicativo existe na lista de aplicativos.
            selected_app = None
            for app in self.applications_list:
                if app.GetName().lower() == app_name.lower():
                    selected_app = app
                    break

            if selected_app:
                print(f"Gerenciando permissões para {selected_app.name}", end='')
                LoadingAnimation(1)
                time.sleep(1) 
                permissions = ["Leitura", "Escrita", "Execução"]
                print(f"Permissões disponíveis: {', '.join(permissions)}")
                time.sleep(1)
                break
            else:
                print(f"O aplicativo '{app_name}' não foi encontrado. Por favor, tente novamente.")
                continue

