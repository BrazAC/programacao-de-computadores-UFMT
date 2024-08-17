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
1 - Obter tres valores
2 - Comparar e obter o menor valor entre os 2 primeiros valores
3 - Comparar e retornar o menor valor entre o menor valor obtido anteriormente com o ultimo valor
'''

def main():
    #1 - Obter os tres valores
    x = int(input("Insira um valor: "))
    y = int(input("Insira um valor: "))
    z = int(input("Insira um valor: "))

    #2 - Comparar e obter o menor valor entre os 2 primeiros valores
    if x <= y:
        menor = x
    else:
        menor = y

    #3 - Comparar e retornar o menor valor entre o menor valor obtido anteriormente com o ultimo valor
    if z <= menor:
        menor = z
    print(f"O menor valor: {menor}")

if __name__ == "__main__":
    main()