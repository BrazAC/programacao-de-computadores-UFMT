def main():
    i, j = [0,0]
    vet = [0]*5
    mtz = [[0]*5 for _ in range(5)]

    while i < 5:
        vet[i] = (i + 1)
        i = i + 1
    
    for i in range(5):
        for j in range(5):
            mtz[i][j] = vet[i] * (i+1)

    #Mostrar vetor e matriz
    print("Vetor: \n", vet)
    print("Matriz")
    for i in range(5):
        print(mtz[i])



if __name__ == "__main__":
    main()