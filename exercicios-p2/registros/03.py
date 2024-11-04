class Registro_Funcionario():
    def __init__(self):
        self.NoFunc = 0
        self.Nome = ''
        self.NoDepend = 0
class Registro_Empresa():
    def __init__(self):
        self.Numero = 0
        self.Nome = ""
def cadastraFunc(listaFunc):
    novoFunc = Registro_Funcionario()
    novoFunc.Nome = input()
    novoFunc.NoFunc = int(input())
    novoFunc.NoDepend = int(input())
    listaFunc.append(novoFunc)
    return listaFunc
def cadastraRH(listaRH):
    novoRH = Registro_Empresa()
    novoRH.Numero = int(input())
    novoRH.Nome = input()
    listaRH.append(novoRH)
    return listaRH
def funcMais3Dep(listaFunc):
    if len(listaFunc) != 0:
        vetMais3 = []
        for func in listaFunc:
            if func.NoDepend > 3:
                vetMais3.append(func)
    else:
        print("Nenhum funcionario cadastrado!")
        return None
    if len(vetMais3) == 0:
        print("Nenhum funcionario com mais de 3 dependentes")
        return None
    else:
        return vetMais3
def main():
    listaRH = []
    listaFunc = []
    while True:
        op = int(input())
        if op == 1:
            listaFunc = cadastraFunc(listaFunc)
        elif op == 2:
            listaRH = cadastraRH(listaRH)
        elif op == 3:
            retorno = funcMais3Dep(listaFunc)
            if retorno != None:
                for func in retorno:
                    print(f"Nome: {func.Nome}")
                    print(f"Numero dependentes: {func.NoDepend}")
        else:
            break
if __name__ == "__main__":
    main()