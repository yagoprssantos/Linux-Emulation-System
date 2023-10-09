import os
import platform

class Refresh:
    def __init__(self):
        pass

    def Fresh(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print("!! Isto é apenas uma simulação !!\n\n")
