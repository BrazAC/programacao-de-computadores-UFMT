def contra(vet):
    if len(vet) == 1:
        print(vet[len(vet) - 1])
    else:
        print(vet[len(vet) - 1])
        vet = [vet[_] for _ in range(0, len(vet) - 1)]
        contra(vet)

vet = [1,2,3,4,5,6,7,8,9,10]
contra(vet)