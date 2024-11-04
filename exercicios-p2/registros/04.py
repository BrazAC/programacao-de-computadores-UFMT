class RegistroFunc():
    def __init__(self):
        self.Nome = ""
        self.Codigo = 0
class RegistroConglomerado():
    def __init__(self):
        self.Empresa1 = []
        self.Empresa2 = []
        self.Empresa3 = []
    def cadastraNaEmpresa(self, func, empresa):
            if empresa == 1:
                self.Empresa1.append(func)
            elif empresa == 2:
                self.Empresa2.append(func)
            elif empresa == 3:
                 self.Empresa3.append(func)
    def encontraFunc(self, codigo):
        funcionario = None
        empresa = ""
        for func in self.Empresa1:
            if func.Codigo == codigo:
                empresa = "Empresa 1"
                funcionario = func
                break
        if funcionario == None:
            for func in self.Empresa2:
                if func.Codigo == codigo:
                    empresa = "Empresa  2"
                    funcionario = func
                    break
            if funcionario == None:
                for func in self.Empresa3:
                    if func.Codigo == codigo:
                        empresa = "Empresa 3"
                        funcionario = func
                        break
        if funcionario == None:
            print("Funcionario nao cadastrado nas empresas")
            return None
        else:
            return (empresa, funcionario)
def main():
    conglomerado = RegistroConglomerado()
    while True:
        op = int(input("MENU, Opção: "))
        if op == 1:
            print("Cadastro funcionario")
            novoFunc = RegistroFunc()
            novoFunc.Nome = input("Nome: ")
            novoFunc.Codigo = int(input("Codigo: "))
            empresa = int(input("Empresa (1, 2, 3): "))
            conglomerado.cadastraNaEmpresa(novoFunc, empresa)
        elif op == 2:
            print("Encontrar funcionario por codigo")
            codigoFunc = int(input("Codigo do funcionario: "))
            retorno = conglomerado.encontraFunc(codigoFunc)
            if retorno != None:
                print(f"Nome: {retorno[1].Nome}")
                print(f"Empresa: {retorno[0]}")
                print(f"Codigo: {retorno[1].Codigo}")
        else:
            break
if __name__ == "__main__":
    main()