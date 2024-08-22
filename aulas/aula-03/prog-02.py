"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
22/08/2024

Programa:
Programa1: Escreva um algoritmo que crie uma matriz de ordem 5x5, 
sorteie números inteiros e preencha esta matriz com os números sorteados. 
Ao final imprima a matriz preenchida por coluna.
"""

#Importando biblioteca random
import random

def main():
    #Criando matriz
    matriz = [[], [], [], [], []]

    #Preenchendo matriz
    for linha in range(0, 5):
        for coluna in range(0, 5):
            matriz[linha].append(random.randrange(1, 11))
    print(matriz)

    #Mostrando matriz por colunas
    for coluna in range (0, 5):
        print(f"\nColuna {coluna}")
        for linha in range(0, 5):
            print(matriz[linha][coluna])
        


if __name__ == "__main__":
    main()