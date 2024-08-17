"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
17/08/2024

Programa:
Pesquise sobre a função min() e max() de Python e refaça os exercícios 2 e 3 usando-as.
"""

#Algoritmo
'''
1 - Obter os tres valores e guardalas em uma lista
2 - Retornar o maior valor usando a funcao max() passando como argumento a lista
3 - Retornar o menor valor usando a funcao min() passando como argumento a lista
'''

def main():
    #1 - Obter os tres valores e guardaos em uma lista
    x = int(input("Insira um valor: "))
    y = int(input("Insira um valor: "))
    z = int(input("Insira um valor: "))
    valores = [x, y, z]

    #2 - Retornar o maior valor usando a funcao max() passando como argumento a lista
    print(f"O maior valor e: {max(valores)}")

    #3 - Retornar o menor valor usando a funcao min() passando como argumento a lista
    print(f"O maior valor e: {min(valores)}")
    

if __name__ == "__main__":
    main()