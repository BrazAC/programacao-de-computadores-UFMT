class Registro_Aluno():
    def __init__(self):
        self.NomeAluno = ""
        self.Idade = 0

def encontraVelho(listaAlunos):
    idade = listaAlunos[0].Idade
    mais_Velhos = []
    for aluno in listaAlunos:
        if aluno.Idade > idade:
            idade = aluno.Idade
    for aluno in listaAlunos:
        if aluno.Idade == idade:
            mais_Velhos.append(aluno)
    return mais_Velhos

def encontraNovo(listaAlunos):
    idade = listaAlunos[0].Idade
    mais_Novos = []
    for aluno in listaAlunos:
        if aluno.Idade < idade:
            idade = aluno.Idade
    for aluno in listaAlunos:
        if aluno.Idade == idade:
            mais_Novos.append(aluno)
    return mais_Novos

def main():
    aluno1 = Registro_Aluno()
    aluno1.NomeAluno = "Braz"
    aluno1.Idade = 10
    aluno2 = Registro_Aluno()
    aluno2.NomeAluno = "Ana"
    aluno2.Idade = 21
    aluno3 = Registro_Aluno()
    aluno3.NomeAluno = "Bia"
    aluno3.Idade = 32
    aluno4 = Registro_Aluno()
    aluno4.NomeAluno = "Camila"
    aluno4.Idade = 11
    aluno5 = Registro_Aluno()
    aluno5.NomeAluno = "Pedro"
    aluno5.Idade = 10

    listaAlunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
    maisNovos = encontraNovo(listaAlunos)
    maisVelhos = encontraVelho(listaAlunos)

    print("Mais novos: ")
    for aluno in maisNovos:
        print(f"Nome: {aluno.NomeAluno}")
        print(f"Idade: {aluno.Idade}")
    print("Mais velhos: ")
    for aluno in maisVelhos:
        print(f"Nome: {aluno.NomeAluno}")
        print(f"Idade: {aluno.Idade}")

if __name__ == "__main__":
    main()