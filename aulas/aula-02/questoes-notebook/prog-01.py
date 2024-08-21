"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
21/08/2024

Programa:
Usando um loop for, escreva um programa que calcule os quadrados e os cubos dos números de 0 a 20. 
Exiba os valores no formato de uma tabela com os números alinhados à direita em cada coluna. 
Use f-string para fazer a formatação.
"""

#Algoritmo
'''
Iterar pela lista de valores de 0 -> 20:
1 - Mostrar valAtual, quadValAtual, cuboValAtual
'''

def main():
    message = ""
    print("_" * 42)
    for valor in range(0, 21, 1):
        #Organizando os numeros
        if valor <= 9:
            message += f'| Valor: {valor}  | '
        else:
            message += f'| Valor: {valor} | '
        #Organizando os quadrados
        if valor**2 < 10:
            message += f'Quadrado: {valor**2}    | '
        elif valor**2 < 100: 
            message += f'Quadrado: {valor**2}   | '
        else:
            message += f'Quadrado: {valor**2}  | '
        #Organizando os cubos
        if valor**3 < 10:
            message += f'Cubo: {valor**3}   | '
        elif valor**3 < 100:
            message += f'Cubo: {valor**3}  | '
        elif valor**3 < 1000:
            message += f'Cubo: {valor**3} | '
        else:
            message += f'Cubo: {valor**3}| '

        print(message)
        message = ""
    print("-" * 42)
if __name__ == "__main__":
    main()