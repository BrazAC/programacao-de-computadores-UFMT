"""
Exercicio:
Calcule a serie de fibonnacci por meio de uma funcao recursiva
Saida:
fibonnacci(0) = 1
fibonnacci(1) = 1
fibonnacci(2) = 2
fibonnacci(3) = 3

Obs:
Serie fibonacci = 0, 1, 1, 2, 3, 5, 8,...
"""
def contCrescente(a):
    if a > 0:
        contCrescente(a - 1)
    print(a, end="")

def fibonacciIterativo(n):
    if n <= 2:
        return 1
    else:
        vet = [1, 1]
        for i in range(2, n):
            vet.append(vet[i-2] + vet[i - 1])
        return vet[n-1]

def fibonacciRecursivo(n):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    else:
        return fibonacciRecursivo(n - 2) + fibonacciRecursivo(n - 1)

def main():
    #print(fibonacciIterativo(6))
    contCrescente(4)
    


if __name__ == "__main__":
    main()