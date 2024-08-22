"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
21/08/2024

Programa:
Para verificar a eficiência de seu automóvel, todas as vezes que enche o tanque, um motorista 
registra os quilômetros percorridos e quantos litros de gasolina foram usados. 
Para ajudá-lo com a análise da eficiência, escreva um programa com repetição controlada por sentinela que 
solicite, a cada iteração, os quilometros percorridos e a gasolina gasta. 

O programa deve calcular e exibir a quilometragem por litro a cada vez que ele encheu o tanque. 
Além disso, depois de processar todas as entradas, 
o programa deve calcular e exibir a quilometragem por litro média, considerando todas as vezes que ele encheu o tanque.
"""

def main():
    kmPercorridos = []
    gasolinaGasta = []
    kmPorL = []
    sentinel = 0
    counter = 0
    while sentinel == 0:
        kmPercorridos.append(float(input("Insert the ammount of Km: "))) 
        gasolinaGasta.append(float(input("Insert the gas used: ")))

        kmPorL.append(kmPercorridos[counter]/gasolinaGasta[counter])
        print(f"KmL in this round: {kmPorL[counter]}")
        counter += 1

        sentinel = int(input("\nInsert 0 to repeat\nInsert other number to stop\n"))
    print(kmPorL)

    soma = 0
    for kmL in kmPorL:
        soma += kmL
    print(f"Median KmL: {soma/len(kmPorL)}")
        

        

if __name__ ==  "__main__":
    main()