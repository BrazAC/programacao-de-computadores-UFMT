def conta(n):
    if n == 1:
        print(n)
    else:
        conta(n - 1)
        print(n)

def main():
    n = int(input("Valor: "))
    conta(n)

if __name__ == "__main__":
    main()