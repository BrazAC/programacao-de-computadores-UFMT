def deconta(n):
    if n == 1:
        print(n)
    else:
        print(n)
        deconta(n - 1)

def main():
    n = int(input("Valor: "))
    deconta(n)

if __name__ == "__main__":
    main()