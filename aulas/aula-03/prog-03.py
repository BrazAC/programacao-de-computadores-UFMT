"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
22/08/2024

Programa:
Programa1: Escreva um algoritmo que crie uma matriz de ordem 5x5, 
sorteie números inteiros e preencha esta matriz com os números sorteados. 
Ao final imprima a matriz preenchida por coluna, depois a diagonal principal
da matriz, depois a diagonal inferior e a diagonal superior
"""

#Importando biblioteca random
import random

'''Funcao que retorna uma matriz 5x5 preenchida com numero aleatorio'''
def criaMatriz(grandeza):
    #Criando matriz
    matriz = [[0]*grandeza for _ in range(grandeza)]

    #Preenchendo matriz
    for linha in range(grandeza):
        for coluna in range(grandeza):
            matriz[linha][coluna] = random.randrange(1, 11)
        print(matriz[linha])
    return matriz

def imprimeDiagPrincipal(matriz, grandeza):
    print("-> Imprimindo diagonal principal")
    for linha in range(grandeza):
        print(matriz[linha][linha])

def imprimePorColuna(matriz, grandeza):
    print("-> Imprimindo por colunas")
    for coluna in range(grandeza):
        print(f"Coluna{coluna}")
        for linha in range(grandeza):
            print(matriz[linha][coluna])

def imprimeDiagSuperior(matriz, grandeza):  
    print("-> Imprimindo diagonal superior")
    for lin in range(grandeza):
        for col in range(lin + 1, grandeza):
            print(matriz[lin][col], end = " ")
        print()
        
def imprimeDiagInferior(matriz, grandeza):
    print("-> Imprimindo diagonal inferior")
    for lin in range(1, grandeza):
        #contador da coluna comeca em 0 e vai ate lin - 1
        for col in range(lin):
            print(matriz[lin][col], end=" ")
        print()

def main():
    
    #Criando matriz
    grandeza = int(input("Qual a grandeza da matriz: "))
    mtz = criaMatriz(grandeza)
    

    #Imprimindo matriz por colunas
    imprimePorColuna(mtz, grandeza)

    #Imprimindo a diagonal principal
    imprimeDiagPrincipal(mtz, grandeza)
    
    #Imprimindo diagonal superior
    imprimeDiagSuperior(mtz, grandeza)

    #Imprimindo diagonal inferior
    imprimeDiagInferior(mtz,grandeza)

if __name__ == "__main__":
    main()