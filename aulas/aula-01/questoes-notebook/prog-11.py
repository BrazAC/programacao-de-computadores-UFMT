"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
18/08/2024

Programa:
Alguns consultores de investimentos dizem que é razoável esperar um retorno de 7% ao ano no longo prazo no mercado de ações. 
Solicite ao usuário o valor investido e calcule quanto dinheiro ele terá após 10, 20 e 30 anos. 
Use a seguinte fórmula para determinar esses valores: a=p(1+r)^n onde p é o valor original investido, 
r é a taxa de retorno anual (7%), n é o número de anos (10, 20 ou 30) e a é o valor obtido no final do enésimo ano.
"""

def main():
    val = float(input("Insira o valor a ser investido: "))
    print(f"Em 10 anos voce tera: {val*(1+7/100)**10}")
    print(f"Em 20 anos voce tera: {val*(1+7/100)**20}")
    print(f"Em 30 anos voce tera: {val*(1+7/100)**30}")


if __name__ == "__main__":
    main()