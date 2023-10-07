import time
from hardware import Hardware

class Server:
    # Classe que fornece serviços a outras máquinas na rede.
    def __init__(self, server_type, ip_address):
        # Inicializa o servidor com um tipo e endereço IP específicos.
        self.server_type = server_type
        self.ip_address = ip_address
        self.machines = []

    def InitializeServer(self):
        # Inicializa o servidor.
        print(f"Servidor {self.server_type} no endereço {self.ip_address} inicializado.")
        time.sleep(2)

    def ShutdownServer(self):
        # Desliga o servidor.
        print(f"Servidor {self.server_type} no endereço {self.ip_address} desligado.")
        time.sleep(2)

    def AddMachine(self, machine):
        # Adiciona uma máquina ao servidor.
        self.machines.append(machine)
        print(f"Máquina adicionada ao servidor no endereço {self.ip_address}.")
        time.sleep(2)
