"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
21/08/2024

Programa:
Para verificar a eficiência de seu automóvel, todas as vezes que enche o tanque, um motorista 
registra os quilômetros percorridos e quantos litros de gasolina foram usados. 
Para ajudá-lo com a análise da eficiência, escreva um programa com repetição controlada por sentinela que 
solicite, a cada iteração, os quilometros percorridos e a gasolina gasta. O programa deve calcular e exibir 
a quilometragem por litro a cada vez que ele encheu o tanque. Além disso, depois de processar todas as entradas, 
o programa deve calcular e exibir a quilometragem por litro média, considerando todas as vezes que ele encheu o tanque.
"""

import random

"""Retorna o dobro do numero"""
def randon(text, seed = 56, *tuplaDados):
    random.seed(seed)
    print(tuplaDados)
    return random.randrange(1, 7)

def main():
    min(2, 3, 4, 5, )
    print(randon("teste", *[1, 2, 3, 4, 5]))

if __name__ ==  "__main__":
    main()