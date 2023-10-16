
# TODO: APAGAR classe Application e juntar com outras funções menores

class Application:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.memory_address = None
        self.running = False
        self.permissions = {
            "Leitura": 1,
            "Escrita": 1,
            "Execução": 1
            } 