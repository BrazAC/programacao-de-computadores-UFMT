"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
17/08/2024

Programa:
Faça um programa capaz de determinar o menor entre três valores inteiros fornecidos pelo usuário.
"""

#Algoritmo
'''
1 - Obter os tres valores
2 - Comparar dois do tres valores, guardar o maior valor
3 - Comparar o maior valor com o ultimo valor, retornar o maior valor
'''

def main():
    #1-Obter os tres valores
    x = int(input("Insira um valor inteiro: "))
    y = int(input("Insira um valor inteiro: "))
    z = int(input("Insira um valor inteiro: "))
    
    #2 - Comparar dois do tres valores, guardar o maior valor
    if x >= y:
        maior = x
    else:
        maior  = y

    #3 - Comparar o maior valor com o ultimo valor, retornar o maior valor
    if maior <= z:
        maior = z
    print(f"O maior valor e: {maior}")

if __name__ == "__main__":
    main()