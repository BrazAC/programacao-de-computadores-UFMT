"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
18/08/2024

Programa:
Usando a fórmula para cálculo de juros compostos, a=p(1+r)^n, 
escreva um programa que com um loop calcula e exibe que você terá a cada ano, de 1 a 30 anos. 
O montante inicial deve ser fornecido pelo usuário.
n = tempo (passado pelo exercicio)
p = valor inicial (o que eu quiser)
r = taxa anual (a que eu quiser)
a = valor resultante
"""

#Algoritmo
"""
Repetir de 0 -> 30:
    mostrar(p * (1 + r) ** n)
"""

def main():
    p = 20
    r = 7
    cont = 1
    while cont <= 30:
        print(p * (1 + r/100) ** cont)
        cont += 1
    print(cont)

if __name__ == "__main__":
    main()