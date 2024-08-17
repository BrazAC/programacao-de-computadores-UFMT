"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
17/08/2024

Programa:
Use um ou mais comandos if para determinar se um número inteiro é ímpar ou par. Dica: Um número par é múltiplo de 2.
"""

#Algoritmo
'''
1 - Receber numero inteiro
2 - Calcular modulo do numero por 2, se o resultado for diferente de zero o numero n e multiplo de dois
    e consequentemente nao e par.
'''

def main():
    valor = int(input("Insira um valor inteiro: "))
    if (valor % 2) != 0:
        print(f"{valor} e impar!")
    else:
        print(f"{valor} e par!")

if __name__ == "__main__":
    main()