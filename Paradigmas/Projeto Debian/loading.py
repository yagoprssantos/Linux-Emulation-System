
import sys, time

# Função meramente ilustrativa para imitar o loading
def Loading_animation(repeat_times=0):
    for _ in range(repeat_times):
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            # Tempo entre os pontos
            time.sleep(1)

        # Clear nos pontos
        sys.stdout.write("\b\b\b   \b\b\b")  
        sys.stdout.flush()
        # Tempo para voltar o loop
        time.sleep(0.5)
    sys.stdout.write("...\n")
