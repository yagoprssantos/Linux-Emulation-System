import time
from loading import LoadingAnimation
from application import *

class ApplicationInterface:
    def __init__(self):
        self.installed_apps = []
        self.running_apps = []

    def AddApplication(self, app_name, app_version):
        new_app = Application(app_name, app_version)
        self.installed_apps.append(new_app)
        print(f"O aplicativo '{app_name}' foi instalado com sucesso!")

    def StartApplication(self, app_index):
        app = self.installed_apps[app_index]
        app_operations = {
            0: lambda: print(f"O aplicativo '{app.name}' já está em execução."),
            1: lambda: print(f"Iniciando o aplicativo '{app.name}' (Versão: {app.version})'{LoadingAnimation(1)}'\nAplicativo '{app.name}' iniciado com sucesso!")
        }
        app_operations[app.running]()

    def StopApplication(self, app_index):
        app = self.installed_apps[app_index]
        app_operations = {
            0: lambda: print(f"O aplicativo '{app.name}' não está em execução."),
            1: lambda: print(f"Parando o aplicativo '{app.name}' (Versão: {app.version})'{LoadingAnimation(1)}'\nAplicativo '{app.name}' parado com sucesso!")
        }
        app_operations[app.running]()

    def ManagePermissions(self, app_index):
        app = self.installed_apps[app_index]
        permissions = ["Leitura", "Escrita", "Execução"]

        while True:
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
                    print(f"Permissão '{permission}' invertida.")
                elif option == 4:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")