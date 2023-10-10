import time
from loading import LoadingAnimation

# TODO: Fazer com que as funções de fato sejam efetivas e funcionais

class SoftwareArchitecture:
    # Classe que define a estrutura e integrações dos componentes de software.
    def __init__(self, software_type, description):
        # Inicializa a arquitetura de software com um tipo específico e descrição.
        self.software_type = software_type
        self.description = description
        self.components = []
        self.integrations = []

    def DefineComponents(self):
        # Define os componentes de software.
        print("Definindo componentes de software", end='')
        LoadingAnimation(1)
        # Adicionando componentes fictícios à lista
        self.components.append("Módulo de Autenticação")
        self.components.append("Serviço de Banco de Dados")
        self.components.append("Biblioteca de Criptografia")
        print("Componentes definidos:")
        for component in self.components:
            print(f"- {component}")
        time.sleep(1)

    def DefineIntegrations(self):
        # Define integrações de software.
        print("Definindo integrações de software", end='')
        LoadingAnimation(1)
        # Adicionando integrações fictícias à lista
        self.integrations.append("API REST para Comunicação entre Módulos")
        self.integrations.append("Barramento de Serviço para Integração de Aplicações")
        self.integrations.append("Middleware de Mensageria para Troca de Mensagens")
        print("Integrações definidas:")
        for integration in self.integrations:
            print(f"- {integration}")
        time.sleep(1)

