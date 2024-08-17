"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
15/08/2024

Programa:
Leia do usuário um valor inteiro positivo (verifique) que irá descrever quantos valores (reais) serão lidos. 
Leia todos os valores previstos. Ao final pergunte ao usuário se é para calcular o produtório ou somatório 
dos valores, imprima todos os valores lidos e calcule a operação desejada.
"""

#Algoritmo
'''
1 - Obter quantos valores serão lidos (int >= 0)
2 - Obter todos os valores e armazená-los em um vetor
3 - Perguntar se o usuario quer calcular somatorio ou produtorio, calcular o desejado
4 - Mostrar todos os valores lidos, mostrar o resultado da operação escolhida
'''

def main():
    #Obter quantos valores serão lidos (int >= 0)
    quantVal = int(input("Insira a quantidade de valores a serem lidos (> 0): "))

    #Verificar se o valor é > 0
    if quantVal <= 0:
        print("Insira uma quantidade valida!")
    else:
        #Obter todos os valores e armazená-los em um vetor
        listaVal = []
        for counter in range(0, quantVal):
            listaVal.append(float(input(f'Insira o valor {counter + 1}: ')))

        #Perguntar se o usuario quer calcular somatorio ou produtorio, calcular o desejado
        opcao = int(input("Quero calcular: 0 (somatorio), 1 (produtorio): "))

        #Mostrar todos os valores lidos, mostrar o resultado da operação escolhida
        print(f'Valores lidos: {listaVal}')
        if opcao :
            #Produtorio
            produtorio = 1
            for valor in listaVal:
                produtorio *= valor
            print(f'Resultado produtorio: {produtorio}')
        else:
            #Somatorio
            somatorio = 0
            for valor in listaVal:
                somatorio += valor
            print(f'Resultado somatorio: {somatorio}')
        


if __name__ == "__main__":
    main()