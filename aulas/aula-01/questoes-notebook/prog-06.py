"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
17/08/2024

Programa:
Solicite ao usuário o valor do raio de um círculo. 
Em seguida exiba o diâmetro, a circunferência e a área. 
Use o valor 3.14159 para π. Use as seguintes fórmulas (r é o raio):

diâmetro=2r
circunferência=2πr
área=πr2
"""

def main():
    r = float(input("Insira o raio do circulo: "))
    pi = 3.14159
    print(f"Diametro: {r * 2}")
    print(f"Circunferencia: {2 * pi * r}")
    print(f"Area: {pi * r ** 2}")    

if __name__ == "__main__":
    main()