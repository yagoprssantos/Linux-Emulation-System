import time, random
from loading import Loading_animation
from kernelLinux import LinuxKernelAPI

class Application:
    # Classe que representa um aplicativo instalado.
    def __init__(self, name):
        # Inicializa um aplicativo com um nome e versão.
        self.name = name
        self.version = round(random.uniform(1.0, 12.0), 1)  # Versão aleatória entre 1.0 e 12.0

    def execute(self):
        # Executa o aplicativo.
        print(f"Executando {self.name}; Versão: {self.version}", end='')
        Loading_animation(1)
        time.sleep(2)

    def get_name(self):
        # Retorna o nome do aplicativo.
        return self.name


class ApplicationInterface:
    # Classe que gerencia a execução e permissões de aplicativos.
    def __init__(self):
        # Inicializa a interface do aplicativo.
        self.applications_list = []

    def add_application(self, application):
        # Adiciona um aplicativo à lista de aplicativos disponíveis.
        self.applications_list.append(application)

    def start_application(self):
        # Pergunta ao usuário qual aplicativo ele deseja abrir.
        while True:
            print("Aplicativos disponíveis:")
            for app in self.applications_list:
                print(app.get_name())

            app_name = input("Digite o nome do aplicativo que deseja abrir: ")

            # Verifica se o aplicativo existe na lista de aplicativos.
            selected_app = None
            for app in self.applications_list:
                if app.get_name().lower() == app_name.lower():
                    selected_app = app
                    break

            if selected_app:
                LinuxKernelAPI.interact_with_kernel()
                selected_app.execute()
                print(f"{selected_app.name} iniciado e pronto para uso.")
                break
            else:
                print(f"O aplicativo '{app_name}' não foi encontrado. Por favor, tente novamente.")
                continue

    def manage_permissions(self):
        # Pergunta ao usuário qual aplicativo ele deseja gerenciar permissões.
        while True:
            print("Aplicativos disponíveis:")
            for app in self.applications_list:
                print(app.get_name())

            app_name = input("Digite o nome do aplicativo para gerenciar permissões: ")

            # Verifica se o aplicativo existe na lista de aplicativos.
            selected_app = None
            for app in self.applications_list:
                if app.get_name().lower() == app_name.lower():
                    selected_app = app
                    break

            if selected_app:
                print(f"Gerenciando permissões para {selected_app.name}", end='')
                Loading_animation(1)
                time.sleep(1) 
                permissions = ["Leitura", "Escrita", "Execução"]
                print(f"Permissões disponíveis: {', '.join(permissions)}")
                time.sleep(1)
                break
            else:
                print(f"O aplicativo '{app_name}' não foi encontrado. Por favor, tente novamente.")
                continue

