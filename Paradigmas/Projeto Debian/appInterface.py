from loading import LoadingAnimation
from application import *
from hardware import *

# TODO: Termine de implementar todas as funções

class ApplicationInterface:
    def __init__(self):
        self.installed_apps = []
        self.running_apps = []
        self.hardware = Hardware()

    def AddApplication(self, app_name, app_version):
        new_app = Application(app_name, app_version)
        self.installed_apps.append(new_app)
        print(f"O aplicativo '{app_name}' foi instalado com sucesso!\n")

    def StartApplication(self, app_index):
        app_name = self.installed_apps[app_index].name
        app_version = self.installed_apps[app_index].version
        app = next((app for app in self.installed_apps if app.name == app_name), None)
        if app is None:
            print(f"O aplicativo '{app_name}' não foi encontrado.")        
        if app.running == True:
            print(f"O aplicativo '{app_name}' já está em execução.")
        else:
            print(f"Iniciando o aplicativo '{app_name}' (Versão: {app_version})", end='')
            LoadingAnimation(1)
            self.hardware.AllocateMemory(app_name)
            app.running = True
            self.running_apps.append(app_name)
            print(f"\nAplicativo '{app_name}' iniciado com sucesso!")

    def StopApplication(self, app_index):
        app_name = self.installed_apps[app_index].name
        app_version = self.installed_apps[app_index].version
        app = next((app for app in self.installed_apps if app.name == app_name), None)
        if app is None:
            print(f"O aplicativo '{app_name}' não foi encontrado.")
        elif app.running == False:
            print(f"O aplicativo '{app_name}' não está em execução.")
        else:
            print(f"Parando o aplicativo '{app_name}' (Versão: {app_version})", end='')
            LoadingAnimation(1)
            Hardware.ReleaseMemory(app_name)
            app.running = False
            self.running_apps.remove(app_name)
            print(f"\nAplicativo '{app_name}' parado com sucesso!")

    def ManagePermissions(self, app_index):
        app = self.installed_apps[app_index]
        permissions = ["Leitura", "Escrita", "Execução"]

        while True:
            self.refresh.Fresh()
            print(f"Permissões para o aplicativo '{app.name}':")
            for i, permission in enumerate(permissions, start=1):
                print(f"{i}. {permission}: {'Ativa' if app.permissions[permission] else 'Desativada'}")

            print("Opções:")
            print("1. Ativar/Desativar permissão de Leitura")
            print("2. Ativar/Desativar permissão de Escrita")
            print("3. Ativar/Desativar permissão de Execução")
            print("4. Voltar ao menu de aplicativos")

            option = input("Escolha uma opção: ")

            if option.isdigit():
                option = int(option)
                if 1 <= option <= len(permissions):
                    permission = permissions[option - 1]
                    app.permissions[permission] = not app.permissions[permission]
                    print(f"Permissão '{permission}' trocada.")
                elif option == 4:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")