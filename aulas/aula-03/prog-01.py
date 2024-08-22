"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
22/08/2024

Programa:
Programa1: Escreva um algoritmo que crie uma matriz de ordem 5x5, sorteie números inteiros e 
preencha esta matriz com os números sorteados. 
Ao final imprima a matriz preenchida.
"""

#Algoritmo
"""
1 - Criar matriz 5x5
2 - Iterar pelos elementos da matriz preenchendo cada espaço com um valor aleatorio

matriz = [[c0,c1,c2,c3,c4], Linha0 
          [c0,c1,c2,c3,c4], Linha1
          [c0,c1,c2,c3,c4], Linha2
          [c0,c1,c2,c3,c4], Linha3
          [c0,c1,c2,c3,c4]] Linha4
"""

#Importando biblioteca random
import random

def main():

    #Criando matriz
    matriz = [[], [], [], [], []]
    
    #Preenchendo matriz
    coluna = 0 
    linha = 0
    while coluna <= 4:
        while linha <= 4:
            numAleatorio = random.randrange(1, 101)
            matriz[coluna].append(numAleatorio) 
            linha += 1
        coluna += 1
        linha = 0
    
    #Mostrando matriz
    for valor in matriz:
        print(valor)

    #matriz[0][0][1]

if __name__ == "__main__":
    main()