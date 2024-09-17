def main():
    #Implementando atividade repetitiva por laço (PROCESSO ITERATIVO)
    """i = 5
    while i > 0:
        print(i)
        i -= 1

    contaDecre(i)"""
    print(fatorial(3))

#Implementando atividade repetitiva por funcao (PROCESSO RECURSIVO)
def contaDecre(i):
    if i > 0:    
        print(i)
        i -= 1
        contaDecre(i)

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

if __name__ == "__main__":
    main()
