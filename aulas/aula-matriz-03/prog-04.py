"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
22/08/2024

Programa:
Programa1: Escreva um algoritmo que crie uma matriz de ordem 5x5, 
sorteie números inteiros e preencha esta matriz com os números sorteados. 
Ao final imprima a matriz preenchida.

Dê continuidade ao Programa 1, de tal forma que você vai implementar um menu, 
com as opções para o usuário imprimir uma célula, ou imprimir uma linha, ou imprimir uma coluna. 
Conforme for a escolha do usuário, faça a ação de desejada, lendo as informações necessárias. 
Verifique se os dados informados para a impressão são válidos.

O programa deve executar o que foi pedido e voltar para o menu 
    (so deve ser finalizado quando 0 for digitado)


Implemente nessa versão a possibilidade usuario decide o tamanho da matriz
"""
#Importando random
import random
import os

#Aqui vem as funcoes a serem usadas
def criaMtz(grandeza):
    #Caso grandeza = 3
    mtx = [[0] * grandeza for _ in range(grandeza)]
   
    for l in range(grandeza):
        for c in range(grandeza):
            mtx[l][c] = random.randrange(1, 11)
    return mtx

def imprimeCelula(linha, coluna, matriz, grandeza):
    if linha >= 0 and linha < grandeza and coluna >= 0 and coluna < grandeza:
        print(f"Valor na celula [{linha}][{coluna}]: {matriz[linha][coluna]}")
    else:
        print("Posicao invalida")  

def imprimeMatriz(matriz, grandeza):
    print("A matriz formada foi:")
    for l in range(grandeza):
        print(matriz[l])
    print("______________________")

def imprimeLinha(matriz, grandeza, linha):
    if linha >= 0 and linha < grandeza:
        print("Sua linha: ", matriz[linha])

def imprimeColuna(matriz, grandeza, coluna):
    col = []
    if coluna >= 0 and coluna < grandeza:
        for linha in range(grandeza):
            col.append(matriz[linha][coluna])
        print("Sua coluna: ", col)

def main():
    print("----====>Boas Vindas<====----")
    print("Insira a grandeza da sua matriz: ")
    grandeza = int(input())
    os.system('clear')

    mtz = criaMtz(grandeza)
    imprimeMatriz(mtz, grandeza)
    escolha = 1

    while escolha != 0:
        print("----====>MENU<====----")
        print("Escolha uma opcao:")
        print("1 - Imprimir celula ")
        print("2 - Imprimir Linha")
        print("3 - Imprimir Coluna")
        print("0 - Sair")
        escolha = int(input())

        os.system('clear')

        if escolha == 1:
            imprimeMatriz(mtz, grandeza)

            print(f"Determine a posicao da celula (deve ser < {grandeza - 1})")
            print(f"Qual a linha: ")
            linha = int(input())
            print("Qual a coluna: ")
            coluna = int(input())
            imprimeCelula(linha, coluna, mtz, grandeza)

            #Voltar ao menu ou finalizar?
            print("---------------------")
            print("\n1 - Voltar ao menu")
            print("0 - Finalizar programa")
            escolha = int(input())
            print("---------------------")
            os.system('clear')
            
        elif escolha == 2:
            imprimeMatriz(mtz, grandeza)

            linha = int(input(f"Insira a linha (deve ser < {grandeza}): "))
            imprimeLinha(mtz, grandeza, linha)

            #Voltar ao menu ou finalizar?
            print("---------------------")
            print("\n1 - Voltar ao menu")
            print("0 - Finalizar programa")
            escolha = int(input())
            print("---------------------")
            os.system('clear')
            
        elif escolha == 3:
            imprimeMatriz(mtz, grandeza)

            coluna = int(input(f"Insira a coluna (deve ser < {grandeza}): "))
            imprimeColuna(mtz, grandeza, coluna)

            #Voltar ao menu ou finalizar?
            print("---------------------")
            print("\n1 - Voltar ao menu")
            print("0 - Finalizar programa")
            escolha = int(input())
            print("---------------------")
            os.system('clear')
            
        elif escolha == 0:
            break
        else:
            print("Insira um opcao valida!")
            
if __name__ == "__main__":
    main()