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
        self.cpu_usage = random.randint(28, 36)

    def CheckHealth(self):
        # Verifica o estado de saúde dos componentes de hardware.
        print("Verificando integridade dos componentes de hardware", end='')
        LoadingAnimation(1)
        LinuxKernelAPI.InteractWithKernel()
        health_list = ["Péssimo", "Ruim", "Ok", "Bom", "Ótimo"] 
        print(f"Saúde do hardware: {random.choice(health_list)}!")
        time.sleep(1)

    def MonitorCPU(self, running_apps):
        # Monitora o uso da CPU.
        print("Monitorando o uso da CPU", end='')
        LoadingAnimation(1)
        LinuxKernelAPI.InteractWithKernel()
        num_running_apps = sum(app.running for app in running_apps)
        if num_running_apps == 0:
            self.cpu_usage = random.randint(28, 36) 
        else:
            self.cpu_usage = min(50 + 10 * (num_running_apps - 1), 100)  # CPU aumenta com base no número de aplicativos em execução.
        print(f"Uso da CPU: {self.cpu_usage}%")
        time.sleep(1)

    def ShowMemoryAllocations(self):
        # Mostra as memórias alocadas e seus endereços.
        print("Memórias alocadas:")
        for app_name, memory_address in self.memory_allocations.items():
            print(f"- '{app_name}': {memory_address}")

    def AllocateMemory(self, app_name):
        # Aloca memória para um aplicativo.
        memory_address = "0x" + ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
        self.memory_allocations[app_name] = memory_address
        print(f"Memória alocada para '{app_name}' no endereço {memory_address}")

    def ReleaseMemory(self, app_name):
        # Libera memória de um aplicativo.
        if app_name in self.memory_allocations:
            del self.memory_allocations[app_name]
            print(f"Memória liberada de '{app_name}'")
        else:
            print(f"Não há alocação de memória para '{app_name}'")

