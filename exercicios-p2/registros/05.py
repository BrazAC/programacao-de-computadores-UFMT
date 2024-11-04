class FICHA_DIA:
    def __init__(self):
        self.DiaSemana = ""
        self.Horas = 0
        self.DiaMes = 0

class FICHA_HORAS_MES():
    def __init__(self):
        self.Nome = ""
        self.Numero = 0
        self.Mes = 0
        self.Dias = []

    def carregaHoras(self, caminhoArquivo):
        arq = open(caminhoArquivo, "r")
        dados = arq.readlines()
        dados = [linha.strip() for linha in dados]
        arq.close()
        novoDia = FICHA_DIA()
        novoDia.DiaSemana = dados[0]
        novoDia.Horas = dados[1]
        novoDia.DiaMes = dados[2]
        self.Dias.append(novoDia)

    def calculaSalario(self):
        valorHora = int(input("Qual o valor da hora: "))
        horasTotais = 0
        for dia in self.Dias:
            horasTotais += dia.Horas
        print(f"Salario total: {horasTotais * valorHora}")

class REGISTRO_FICHARIO():
    def __init__(self):
        self.Numero = 0
        self.Fichas = []

class REGISTRO_GAVETA():
    def __init__(self):
        self.Ficheiros = []

    def mostraSalario(self):
        numFunc = int(input("Numero do funcionario: "))
        numMes = int(input("Numero do mes: "))
        for fichario in self.Ficheiros:
            if fichario.Numero == numFunc:
                for ficha in fichario:
                    if ficha.Mes == numMes:
                        ficha.calculaSalario()
    
    def encontraFuncionario(self, numFunc):
        for fichario in self.Ficheiros:
            if fichario.Numero == numFunc:
                return fichario.Fichas[len(fichario.Fichas) - 1]

def criaFichaPorArquivo(caminhoArquivo):
    arq = open(caminhoArquivo, "r")
    dados = arq.readlines()
    dados = [linha.strip() for linha in dados]
    arq.close()
    novaFicha = FICHA_HORAS_MES()
    for linha in range(len(dados)):
        if dados[linha] == "NOME":
            novaFicha.Nome = dados[linha + 1]
        elif dados[linha] == "NUMERO":
            novaFicha.Numero = dados[linha + 1]
        elif dados[linha] == "MES":
            novaFicha.Mes = dados[linha + 1]
        elif dados[linha] == "DIA":
            novoDia = FICHA_DIA()
            novoDia.DiaSemana = dados[linha + 1]
            novoDia.Horas = dados[linha + 2]
            novoDia.DiaMes = dados[linha + 3]
            novaFicha.Dias.append(novoDia)


            """linha += 1
            while dados[linha] != "":
                if type(dados[linha]) == str:
                    novoDia = FICHA_DIA()
                    novoDia.DiaSemana = dados[linha]
                    novoDia.Horas = dados[linha + 1]
                    novoDia.DiaMes = dados[linha + 2]
                    novaFicha.Dias.append(novoDia)
                linha += 1
            break"""
    return novaFicha
            
            
def main():
    gavetaFichas = REGISTRO_GAVETA()
    while True:
        print("1 - Cadastrar funcionario")
        print("2 - Carregar horas (por arquivo)")
        print("3 - Mostrar todos funcionarios")
        print("4 - Mostrar salario do mes")
        op = int(input("Opcao (1,2,3,4,5): "))
        if op == 1: #Cadastro Funcionario por arquivo
            print("CADASTRO DE FUNCIONARIO")
            """
            novaFichaHoras = FICHA_HORAS_MES()
            novaFichaHoras.Nome = input("Nome: ")
            novaFichaHoras.Numero = int(input("Numero: "))
            novaFichaHoras.Mes = int(input("Mes de entrada: "))
            """
            
            novaFichaHoras = criaFichaPorArquivo("./dadosMes.txt")
            
            novoFichario = REGISTRO_FICHARIO()
            novoFichario.Numero = novaFichaHoras.Numero
            novoFichario.Fichas.append(novaFichaHoras)

            gavetaFichas.Ficheiros.append(novoFichario)
            print("Funcionario cadastrado")

        elif op == 2: #Carregar horas por arquivo
            numFunc = int(input("Numero do funcionario: "))
            fichaHoras = gavetaFichas.encontraFuncionario(numFunc)
            fichaHoras.carregaHoras("./horasDia.txt")
            gavetaFichas.Ficheiros[0].Fichas.remove(fichaHoras)
            gavetaFichas.Ficheiros[0].Fichas.append(fichaHoras)
            print("Horas carregadas")
        
        elif op == 3: #Mostrar funcionarios
            for fichario in gavetaFichas.Ficheiros:
                print(f"Numero funcionario: {fichario.Numero}")
                for ficha in fichario.Fichas:
                    print(f"Ficha do mes {ficha.Mes}")
                    print(f"Nome do funcionario: {ficha.Nome}")
                    for dia in ficha.Dias:
                        print(f"Dia: {dia.DiaSemana}")
                        print(f"Horas trabalhadas {dia.Horas}")

        elif op == 4: #Mostrar salario do mes
            gavetaFichas.mostraSalario()
            

        else:
            break


if __name__ == "__main__":
    main()