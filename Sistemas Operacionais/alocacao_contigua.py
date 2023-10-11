"""

**Integrantes do grupo:**

Ana Luiza
Bruna
Gabriela
Leonardo
Yago

"""

def AlocacaoContigua(algorithm):
    # Define as partições de memória iniciais com seus tamanhos
    memoria = {"m1": 10, "m2": 5, "m3": 6, "m4": 1}
    # Define os tamanhos dos programas a serem alocados
    programas = {"y": 5, "a": 7, "g": 1, "o": 4}

    print(f"\n\n{'='*45}\n{'ALOCAÇÃO CONTÍGUA - ' + algorithm.upper()}\n")
    # Imprime o tamanho de todas as partições após cada alocação
    partitions_info_i = " // ".join([f"{particao} - {tamanho}K" for particao, tamanho in memoria.items()])
    print(f"Tamanhos iniciais das Partições:\n{partitions_info_i}\n{'='*45}")

    for programa, tamanho_programa in programas.items():
        if algorithm == "best fit":
            sorted_memoria = sorted(memoria.items(), key=lambda x: x[1])
        elif algorithm == "worst fit":
            sorted_memoria = sorted(memoria.items(), key=lambda x: x[1], reverse=True)
        elif algorithm == "first fit":
            sorted_memoria = memoria.items()
        else:
            print("Algoritmo não encontrado. Tente novamente.")
            return
        
        alocado = False
      
        for particao, tamanho_particao in sorted_memoria:
            if tamanho_particao >= tamanho_programa:
                memoria[particao] -= tamanho_programa  # Aloca a memória
                alocado = True
                break  # Interrompe a busca por uma partição assim que for alocada

        if alocado:
            print(f"Programa '{programa}' ({tamanho_programa}K) alocado na partição '{particao}'.\n")
        else:
            print(f"Não foi possível alocar o Programa '{programa}' ({tamanho_programa}K).")
        
        # Imprime o tamanho de todas as partições após cada alocação
        partitions_info_f = " // ".join([f"{particao} - {tamanho}K" for particao, tamanho in memoria.items()])
        print("Tamanhos das Partições: \n" + partitions_info_f)
        print('-'*45)  # Adiciona uma barra horizontal para separar os resultados

# Exibindo informações iniciais
print(("\npartições livres: 10K, 5K, 6K e 1K\n").upper())
print(("\nrequisições entram na seguinte ordem:"
      "\n1º- Programa Y (5K)"
      "\n2º- Programa A (7K)"
      "\n3º- Programa G (1K)"
      "\n4º- Programa O (4K)\n").upper())

def main():
    print("=== MENU DE ALGORITMOS DE ALOCAÇÃO ===")
    print("1. Best-Fit")
    print("2. Worst-Fit")
    print("3. First-Fit")
    print("4. Todos os algoritmos")

    choice = input("Escolha o algoritmo (1/2/3/4): ")

    if choice == "1":
        AlocacaoContigua("best fit")
    elif choice == "2":
        AlocacaoContigua("worst fit")
    elif choice == "3":
        AlocacaoContigua("first fit")
    elif choice == "4":
        AlocacaoContigua("first fit")
        AlocacaoContigua("best fit")
        AlocacaoContigua("worst fit")
    else:
        print("Opção inválida. Escolha um número de 1 a 4.")        

if __name__ == "__main__":
    main()