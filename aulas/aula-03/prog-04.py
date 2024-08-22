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


Implemente nessa versão a possibilidade usuario decide o tamanho da 
"""
#Importando random
import random




#Aqui vem as funcoes a serem usadas
def criaMtz(grandeza):
    #Caso grandeza = 3
    mtx = [[0] * grandeza] * grandeza
   
    print(mtx) 

def main():
    escolha = 1
    criaMtz(3)
    while escolha != 0:
        print("--------------------- \nEscolha uma opcao: ")
        print("1 - Imprimir celula \n2 - Imprimir Linha \n3 - Imprimir Coluna \n0 - Sair")
        escolha = int(input())

        if escolha == 1:
            print("Escolheu 1")
            #Verificar se a posicao existe na matriz
            #Executar funcao que mostra celula (um elemento da matriz)
            
        elif escolha == 2:
            print("Escolheu 2")
            #Verificar se a posicao existe na matriz
            #Perguntar qual linha
            #Executar funcao que mostra linha requerida
            
        elif escolha == 3:
            print("Escolheu 3")
            #Verificar se a posicao existe na matriz
            #Perguntar qual coluna
            #Executar funcao que mostra coluna requerida
            
        elif escolha == 0:
            break
        else:
            print("Insira um opcao valida!")
            
        



if __name__ == "__main__":
    main()