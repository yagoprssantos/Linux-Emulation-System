from hardware import Hardware

class Machine:
    # Classe que representa uma máquina física ou virtual.
    def __init__(self, machine_type, description):
        # Inicializa uma máquina com um tipo e descrição específicos.
        self.machine_type = machine_type
        self.description = description
        self.system_hardware = Hardware("Intel i7", "16GB", "1TB SSD")
