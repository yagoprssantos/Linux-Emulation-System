import os, platform

# TODO: APAGAR classe Refresh e juntar Fresh com outras funções menores

class Refresh:
    def __init__(self):
        pass

    def Fresh(self):
        # Classe que faz uma limpa no terminal
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print("!! Isto é apenas uma simulação !!\n")
