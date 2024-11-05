def sum(a, b):
    if b == 1:
        return a + b
    else:
        return sum(a, b - 1) + 1

def main():
    a = int(input("Insira a: "))
    b = int(input("Insira b: "))
    print(sum(a, b))
    
if __name__ == "__main__":
    main()