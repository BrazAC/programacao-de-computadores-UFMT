"""
UFMT - Campus Araguaia
Aluno: Braz Amorim Campos
Data: 05/09/2024
Professor: Ivairton


Exercicio:
Calcule a serie de fibonnacci por meio de uma funcao recursiva
Saida:
fibonnacci(0) = 1
fibonnacci(1) = 1
fibonnacci(2) = 2
fibonnacci(3) = 3

Obs:
Serie fibonacci = 1, 1, 2, 3, 5, 8,...
"""

def main():
    posicao = 5
    print(fibonacci(posicao - 1))

def fibonacci(posicaoAlvo):
    #Mostrar valor na posicaoAlvo da sequencia
    if posicaoAlvo == 0:
        return 1
    elif posicaoAlvo == 1:
        return 1
    else:
        termo = fibonacci(posicaoAlvo-1) + fibonacci(posicaoAlvo-2)
        return termo
        


if __name__ == "__main__":
    main()