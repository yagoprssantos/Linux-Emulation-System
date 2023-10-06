import time, random
from loading import Loading_animation
from kernelLinux import LinuxKernelAPI

class Hardware:
    # Classe que representa os componentes de hardware de uma máquina.
    def __init__(self, cpu, memory, storage):
        # Inicializa os componentes de hardware: CPU, memória e armazenamento.
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def check_health(self):
        # Verifica o estado de saúde dos componentes de hardware.
        print("Verificando integridade dos componentes de hardware", end='')
        Loading_animation(1)
        LinuxKernelAPI.interact_with_kernel()
        health_list = ["Péssimo", "Ruim", "Ok", "Bom", "Ótimo"] 
        print(f"Saúde do hardware: {random.choice(health_list)}!")
        time.sleep(1)

    def monitor_cpu_usage(self):
        # Monitora o uso da CPU.
        print("Monitorando o uso da CPU", end='')
        Loading_animation(1)
        LinuxKernelAPI.interact_with_kernel()
        cpu_usage = random.randint(10, 90)  # Simula o uso aleatório da CPU
        print(f"Uso da CPU: {cpu_usage}%")
        time.sleep(1)

    def manage_memory(self):
        # Gerencia os recursos de memória.
        print("Gerenciando os recursos de memória", end='')
        Loading_animation(1)
        LinuxKernelAPI.interact_with_kernel()
        
        # Simula a alocação e liberação de memória para um processo fictício
        allocated_memory = random.randint(1, 16)  # em GB
        print(f"Alocando {allocated_memory}GB de memória para um processo fictício.")
        Loading_animation(2)
        time.sleep(1)
        
        print(f"Liberando {allocated_memory}GB de memória após o término do processo.")
        Loading_animation(1)
        time.sleep(1)


class SoftwareArchitecture:
    # Classe que define a estrutura e integrações dos componentes de software.
    def __init__(self, software_type, description):
        # Inicializa a arquitetura de software com um tipo específico e descrição.
        self.software_type = software_type
        self.description = description
        self.components = []
        self.integrations = []

    def define_components(self):
        # Define os componentes de software.
        print("Definindo componentes de software", end='')
        Loading_animation(1)
        # Adicionando componentes fictícios à lista
        self.components.append("Módulo de Autenticação")
        self.components.append("Serviço de Banco de Dados")
        self.components.append("Biblioteca de Criptografia")
        print("Componentes definidos:")
        for component in self.components:
            print(f"- {component}")
        time.sleep(1)

    def define_integrations(self):
        # Define integrações de software.
        print("Definindo integrações de software", end='')
        Loading_animation(1)
        # Adicionando integrações fictícias à lista
        self.integrations.append("API REST para Comunicação entre Módulos")
        self.integrations.append("Barramento de Serviço para Integração de Aplicações")
        self.integrations.append("Middleware de Mensageria para Troca de Mensagens")
        print("Integrações definidas:")
        for integration in self.integrations:
            print(f"- {integration}")
        time.sleep(1)

