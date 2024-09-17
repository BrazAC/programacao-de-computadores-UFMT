def main():
    i = 5

    print("Ordem crescente na descida")
    mostraValCrescEmpi(i, i)

    print("Ordem decrescente na subida")
    mostaValDecrDesemp(i)

    print("Ordem crescente na subida")
    mostaValCrescDesemp(i)

#Funcoes recursivas
#Funcao que mostra valores na ordem decrescente, durante o empilhamento de processos
def mostraValDecrEmpi(i):
    if i >= 0:
        print(i)
        mostraValDecrEmpi(i - 1)

#Funcao que mostra valores na ordem crescente, durante o empilhamento de processos
def mostraValCrescEmpi(i, c):
    if c >= 0:
        print(i - c)
        c -= 1 
        mostraValCrescEmpi(i, c)

#Funcao que mostra valores na ordem decescente, durante o desempilhamento de processos
def mostaValDecrDesemp(i):
    if i >= 0:
        print(i)
        i -= 1
        mostaValDecrDesemp(i)

#Funcao que mostra valores na ordem crescente, durante o desempilhamento de processos <--AFAZER
def mostaValCrescDesemp(i):
    if i >= 0:
        j = i
        i -= 1
        mostaValDecrDesemp(i)
        print(j)


if __name__ == "__main__":
    main()