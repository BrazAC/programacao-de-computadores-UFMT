def fat(n):
    if n == 1:
        return n
    else:
        return fat(n - 1) * n
def main():
    n = int(input("Valor: "))
    print(fat(n))

if __name__ == "__main__":
    main()