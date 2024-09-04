"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
22/08/2024

Programa:
Um palíndromo é um número, palavra ou frase de texto que é igual quando lida de trás para frente. 
Por exemplo, cada um dos seguintes números inteiros de cinco dígitos é um palíndromo: 12321, 55555, 45554 e 11611. 

Escreva um programa que leia um número inteiro de cinco dígitos e determine se é um palíndromo. 
[Dica: use os operadores // e % para separar o número em seus dígitos.]
"""
#ALgoritmo
'''
1 - Separar o numero em algarismos e guardar em uma lista
2 - Verificar se o numero e um palindromo:
    2.1 - Se o primeiro algarismo for igual ao ultimo
    2.2 - Se o segundo algarismo for igual ao penultimo



1 - 
cont = 4
Repetir enquanto cont >= 0 
    Dividir (//) o numero por 10**cont adicionar o valor obtido ao final da lista algarismos
    Subtrair do numero (-) algarismo*10**cont, guardar o valor em numero 
    cont -= 1
'''

def main():
    valor = int(input("Insira um valor de 5 digitos:"))

    #Separando numero em algarismos e guardando em uma lista
    algarismos = []
    cont = 4
    for j in range(5):
        algarismo = valor // 10**cont
        algarismos.append(algarismo)
        valor -= algarismos[j]*10**cont
        cont -= 1
    print(algarismos)

    #Verificando se e um palindromo
    if algarismos[0] == algarismos[4] and algarismos[1] == algarismos[3]:
        print("E palindromo")
    else:
        print("Nao e palindromo")

if __name__ == "__main__":
    main()