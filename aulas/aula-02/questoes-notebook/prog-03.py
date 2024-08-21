"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
18/08/2024

Programa:
Escreva um programa que extraia os dígitos de um número inteiro de cinco dígitos. 
Use um loop que em cada iteração e obtenha cada um dos dígitos (da esquerda para a direita) 
usando os operadores // e % e, em seguida, exiba esse dígito.
"""

#Algoritmo
'''
val = valor do usuario de 5 digitos
quantDigit = 5
cont = quantDigit - 1
repetir enquanto val > 0 
    alg = val // 10**cont
    mostrar alg
    val -= alg * 10**cont
    cont -= 1
'''

def main():
    val = int(input("Insira um numero de 5 digitos: "))
    quantDigit = 5
    cont = quantDigit - 1
    while val > 0:
        alg = val // 10**cont
        print(alg, end="   ")
        val -= alg * 10**cont
        cont -= 1
    print("")
if __name__ == "__main__":
    main()