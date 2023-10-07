import time, random
from loading import LoadingAnimation
from kernel import LinuxKernelAPI

class Hardware:
    # Classe que representa os componentes de hardware de uma máquina.
    def __init__(self, cpu, memory, storage):
        # Inicializa os componentes de hardware: CPU, memória e armazenamento.
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def CheckHealth(self):
        # Verifica o estado de saúde dos componentes de hardware.
        print("Verificando integridade dos componentes de hardware", end='')
        LoadingAnimation(1)
        LinuxKernelAPI.InteractWithKernel()
        health_list = ["Péssimo", "Ruim", "Ok", "Bom", "Ótimo"] 
        print(f"Saúde do hardware: {random.choice(health_list)}!")
        time.sleep(1)

    def MonitorCPU(self):
        # Monitora o uso da CPU.
        print("Monitorando o uso da CPU", end='')
        LoadingAnimation(1)
        LinuxKernelAPI.InteractWithKernel()
        cpu_usage = random.randint(10, 90)  # Simula o uso aleatório da CPU
        print(f"Uso da CPU: {cpu_usage}%")
        time.sleep(1)

    def ManageMemory(self):
        # Gerencia os recursos de memória.
        print("Gerenciando os recursos de memória", end='')
        LoadingAnimation(1)
        LinuxKernelAPI.InteractWithKernel()
        
        # Simula a alocação e liberação de memória para um processo fictício
        allocated_memory = random.randint(1, 16)  # em GB
        print(f"Alocando {allocated_memory}GB de memória para um processo fictício.")
        LoadingAnimation(2)
        time.sleep(1)
        
        print(f"Liberando {allocated_memory}GB de memória após o término do processo.")
        LoadingAnimation(1)
        time.sleep(1)

