def prod(a, b):
    if b == 1:
        return a
    else:
        return prod(a, b - 1) + a

def main():
    a = int(input("Insira a: "))
    b = int(input("Insira b: "))
    print(prod(a, b))

if __name__ == "__main__":
    main()