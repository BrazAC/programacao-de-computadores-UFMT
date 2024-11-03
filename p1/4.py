
def mostraSeq(n):
    seq = [1,1]
    for i in range(2, n):
        seq.append(seq[i-2] + seq[i-1])
    print(seq)

def main():
    n = int(input())
    mostraSeq(n)
    if n == 1: 
        print(1)
    elif n == 2:
        print([1, 1])
    else:
        mostraSeq(n)

"""
def mostraSeq(n):
    seq = [1,1]
    if n == 0:
        print("Numero deve ser maior igual a 1!")
    elif n == 1:
        print(seq[0])
    elif n == 2:
        print(seq)
    else:
        for i in range(2, n):
            seq.append(seq[i-2] + seq[i-1])
        print(seq)

def main():
    n = int(input())
    mostraSeq(n)
    """
    

if __name__ == "__main__":
    main()