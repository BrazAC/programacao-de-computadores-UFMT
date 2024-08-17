"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
17/08/2024

Programa:
Escreva um script que solicite três números inteiros ao usuário. 
Então, exiba a soma, a média, o produto, o menor e o maior dos números.
"""

#ALgoritmo
'''
1 - Obter tres numeros inteiros
2 - Mostrar o somatorio, produtorio, media do numeros
3 - Analisar e mostrar o menor e o maior dos numeros
'''

def main():
    #1 - Obter tres numeros inteiros
    x = int(input("Insira um valor inteiro: "))
    y = int(input("Insira um valor inteiro: "))
    z = int(input("Insira um valor inteiro: "))

    #2 - Mostrar o somatorio, produtorio, media do numeros
    print(f'\nO somatorio dos numeros: {x + y + z}')
    print(f'O produtorio dos numeros: {x * y * z}')
    print(f"A media entre os numeros: {(x + y + z)/3}\n")

    #3 - Analisar e mostrar o menor e o maior dos numeros
    #Menor valor
    if x <= y:
        menor = x
        if menor >= z:
            print(f"O menor valor: {z}")
        else:
            print(f"O menor valor: {menor}")
    else:
        menor = y
        if menor >= z:
            print(f"O menor valor: {z}")
        else:
            print(f"O menor valor: {menor}")
    
    #Maior valor
    if x >= y:
        maior = x
        if maior <= z:
            print(f"O maior valor: {z}")
        else:
            print(f"O maior valor: {maior}")
    else:
        maior = y
        if maior <= z:
            print(f"O maior valor: {z}")
        else:
            print(f"O maior valor: {maior}")


if __name__ == "__main__":
    main()