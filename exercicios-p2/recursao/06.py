def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    n = int(input("Valor: "))
    print([fib(i) for i in range(n)])

if __name__ == "__main__":
    main()