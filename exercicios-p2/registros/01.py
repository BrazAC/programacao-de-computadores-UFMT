class Registro__FUNC():
    def __init__(self):
        self.NoFunc = 0
        self.Nome = ""
        self.DataNasc = 0

def main():
    listaFunc = []
    sent = True
    while sent:
        op = int(input())
        if op == 1:
            novoFunc = Registro__FUNC()
            novoFunc.NoFunc = int(input())
            novoFunc.Nome = input()
            novoFunc.DataNasc = int(input())
            listaFunc.append(novoFunc)
        elif op == 2:
            if len(listaFunc) != 0:
                numCad = int(input())
                cont = 0
                for i in range(len(listaFunc)):
                    if listaFunc[i].NoFunc == numCad:
                        print(f"Numero: {listaFunc[i].NoFunc}")
                        print(f"Nome: {listaFunc[i].Nome}")
                        print(f"Data nascimento: {listaFunc[i].DataNasc}")
                        cont += 1
                if cont == 0:
                    print("Func nao cadastrado")
            else:
                print("Nenhum func cadastrado")
        else:
            sent = False

if __name__ == "__main__":
    main()