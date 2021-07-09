# class Carro:
#     def __init__(self, marca, cor, potencia):
#         self.marca = marca
#         self.cor = cor
#         self.potencia = potencia

#     def Ligar(self):
#         print('Ligando')

#     def Desligar(self):
#         print('desligando')

#     def InfosCar(self):
#         print(self.marca, self.cor, self.potencia)

# carro1 = Carro('ford', 'vermelho', 1.0)

# carro1.Desligar()

# carro1.Ligar()

# carro1.InfosCar()


# def menu():
#     continuar=1

#     while continuar:
#         continuar = int(
#             input("0. Sair\n"+
#                   "1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n"+
#                   "2. Inserir aluno e nota\n"+
#                   "3. Alterar a nota de um aluno\n"+
#                   "4. Consultar nota de um aluno específico\n"+
#                   "5. Apagar um aluno da lista\n"+
#                   "6. Dar a média da turma\n"))
#         if continuar==1:
#             exibir()
#         elif continuar == 2:
#             inserir()
#         elif continuar == 3:
#             alterar()
#         elif continuar == 4:
#             consultar()
#         elif continuar == 5:
#             apagar()
#         elif continuar == 6:
#             media()
#         elif continuar == 0:
#             print("Encerrando programa")
#         else:
#             print("Opção inválida")

# def exibir():
#     for nome in alunos.keys():
#         print("Nome: ", nome, " - Nota: ", alunos[nome])

# def inserir():
#     nome = input("Digite o nome do aluno: ")
#     nota = float(input("Nota dele: "))

#     if alunos.get(nome):
#         print("Ja existe o aluno ",nome)
#     else:
#         alunos[nome] = nota

# def alterar():
#     nome = input("Aluno a mudar a nota: ")
#     nota = float(input("Nova nota     : "))

#     if nome in alunos.keys():
#         alunos[nome] = nota
#     else:
#         print("Não existe esse aluno")

# def consultar():
#     nome = input("Digite o nome do aluno: ")

#     if alunos.get(nome):
#         print("Nota de ",nome, ": ", alunos[nome])
#     else:
#         print("Nao existe tal aluno")

# def apagar():
#     nome = input("Apagar que aluno: ")

#     if alunos.get(nome):
#         alunos.pop(nome)
#     else:
#         print("Não existe o aluno ",nome)

# def media():
#     soma = 0
#     for count in alunos.values():
#         soma += count
#     print("Média dos alunos: %.2f" % (soma / len(alunos) ))

# alunos = {}
# menu()


# faz o relatório de todas as discuplinas!
# RelatorioDisciplinas = []

# def relatorioDisciplinas:
#     for i

class Disciplina:
    def __init__(self, nomeDisciplina, codigo):
        self.nomeDisciplina = nomeDisciplina
        self.codigo = codigo
        self.alunos = []

    def associar_aluno(self, aluno, nota1, nota2):
        self.alunos.append([aluno, nota1, nota2])

    def relatorio(self):
        if(len(self.alunos) == 0):
            print('Disciplina sem alunos matriculados')
        else:
            print('Matric | Nome | Prova 1 | Prova 2')
            for aluno in self.alunos:
                print(f'{aluno[0].matricula} | {aluno[0].nome} | {aluno[1]} | {aluno[2]}')


class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.disciplinas = []

    def cadastrar_disciplinas(self, disciplina, nota1, nota2):
        self.disciplinas.append([disciplina, nota1, nota2])

    def consultar_disciplinas(self):
        if(len(self.disciplinas) == 0):
            print('Aluno sem disciplinas matriculadas')
        else:
            print('Matriculado em:')
            for i in self.disciplinas:
                print(f'|{i[0].codigo}|{i[0].nomeDisciplina} | prova 1: {i[1]} | prova 2: {i[2]} |')
                print('---------------------------------------------')


def menu():
    continuar = 1

    while continuar:
        continuar = int(
            input("0. Sair\n" +
                  "1. Exibir relatório de disciplinas\n" +
                  "2. Inserir aluno\n" +
                  "3. Inserir Disciplina \n" +
                  "4. Matricular aluno em uma disciplina\n" +
                  "5. Apagar um aluno da lista\n" +
                  "6. Dar a média da turma\n"))
        if continuar == 1:
            exibirRelatorio()
        elif continuar == 2:
            inserirAluno()
        elif continuar == 3:
            inserirDisciplina()
        elif continuar == 4:
            MatricularAluno()
        elif continuar == 5:
            apagar()
        elif continuar == 6:
            media()
        elif continuar == 0:
            print("Encerrando programa")
        else:
            print("Opção inválida")


RelatorioDisciplinas = []
AlunosMatriculados = []


def exibirRelatorio():
    for i in RelatorioDisciplinas:
        print()


def inserirAluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno (somente números): ")
    q = 1
    while q == 1:
        error = []
        if not idade.isdigit():
            idade = input("Digite a idade do aluno (somente números): ")
            error.append(idade)
        # if int(idade) < 0:
        #     print('Apenas números positivos!')
        #     idade = str(input("Digite a idade do aluno (somente números): "))
        #     error.append(idade)
        if len(error) == 0:
            q = 0
    f = 1
    while f == 1:
        matricula = 'a'+input("Digite a matrícula do aluno: ")
        print(matricula)
        # nota = float(input("Nota dele: "))
        erro = 0
        for aluno in AlunosMatriculados:
            if matricula == aluno[0]:
                erro = 1
        if erro != 0:
            print("Ja existe o aluno com essa matrícula: ", matricula)
        else:
            AlunosMatriculados.append([matricula, nome, idade, matricula])
            for aluno in AlunosMatriculados:
                if matricula == aluno[0]:
                    aluno[3] = Aluno(nome, idade, matricula)
            f = 0
            print(AlunosMatriculados)

    # matricula.consultar_disciplinas()


def inserirDisciplina():
    nomeDisciplina = input("Nome da disciplina: ")
    for disciplina in RelatorioDisciplinas:
        if nomeDisciplina in disciplina[1]:
            print("Disciplina já cadastrada")
            return
    c = 1
    while c == 1:
        erro = []
        codigo ='d'+input("Código da disciplina: ")
        for disciplina in RelatorioDisciplinas:
            if codigo in disciplina[0]:
                print("Código já existe na base de dados")
                erro.append('codigo')
        if(len(erro) == 0):
            c = 0
    
    RelatorioDisciplinas.append([codigo, nomeDisciplina, codigo])
    for disciplina in RelatorioDisciplinas:
        if codigo == disciplina[0]:
            disciplina[2] = Disciplina(nomeDisciplina, codigo)
    print(RelatorioDisciplinas)


def MatricularAluno():
    if(len(RelatorioDisciplinas) == 0):
        print("Nenhuma discuplina cadastrada!")
        return
    if(len(AlunosMatriculados) == 0):
        print("Nenhum aluno cadastrado!")
        return

    print("Cód | Disciplina")
    for d in RelatorioDisciplinas:
        print(f'{d[0]} | {d[1]}')
        print("------------------------")
    d = 1
    while d == 1:
        erro = []
        disciplina = input("Digite o código da disciplina: ")
        for disc in RelatorioDisciplinas:
            if disciplina == disc[0]:
                d = 0
                erro = []
                break
            else:
                erro.append('disciplina')
        if(len(erro) != 0):
            print('Código inexistente')

    print("Matric | Nome")
    for a in AlunosMatriculados:
        print(f'{a[0]} | {a[1]}')
        print("------------------------")
    al = 1
    while al == 1:
        erro = []
        aluno = input("Digite a matrícula do aluno: ")
        for alun in AlunosMatriculados:
            if aluno == alun[0]:
                al = 0
                erro = []
                break
            else:
                erro.append('aluno')
        if(len(erro) != 0):
            print('Matrícula inexistente')

    nt1 = 1
    while nt1 == 1:
        erro = []
        nota1 = input("Nota da primeira prova (somente números): ")
        if not nota1.isdigit():
            erro.append('nota')
        if(len(erro) == 0):
            nt1 = 0

    nt2 = 1
    while nt2 == 1:
        erro = []
        nota2 = input("Nota da primeira prova (somente números): ")
        if not nota2.isdigit():
            erro.append('nota')
        if(len(erro) == 0):
            nt2 = 0
    
    for a in AlunosMatriculados:
        if aluno == a[0]:
            for d in RelatorioDisciplinas:
                if disciplina == d[0]:
                    disc = d[2]
            a[3].cadastrar_disciplinas(disc, nota1, nota2)
            a[3].consultar_disciplinas()

    for d in RelatorioDisciplinas:
        if disciplina == d[0]:
            for a in AlunosMatriculados:
                if aluno == a[0]:
                    al = a[3]
            d[2].associar_aluno(al, nota1, nota2)
            d[2].relatorio()

    # print(aluno, nomeAluno, nota1, nota2)
    # print()
    # print(nomeDisciplina, disciplina, nota1, nota2)


    # disciplina.relatorio()
    # # disciplina.associar_aluno(aluno, nomeAluno, nota1, nota2)
    
    # aluno.cadastrar_disciplinas(nomeDisciplina, disciplina, nota1, nota2)

    # disciplina.relatorio()
    # aluno.consultar_disciplinas()














def consultar():
    nome = input("Digite o nome do aluno: ")

    if alunos.get(nome):
        print("Nota de ", nome, ": ", alunos[nome])
    else:
        print("Nao existe tal aluno")


def apagar():
    nome = input("Apagar que aluno: ")

    if alunos.get(nome):
        alunos.pop(nome)
    else:
        print("Não existe o aluno ", nome)


def media():
    soma = 0
    for count in alunos.values():
        soma += count
    print("Média dos alunos: %.2f" % (soma / len(alunos)))


alunos = {}
menu()



# a123 = Aluno('marco', 15, 123)
# d147 = Disciplina('Matemática', 147)

# d147.associar_aluno(a123, 5, 6)
# a123.cadastrar_disciplinas(d147, 5, 6)

# d147.relatorio()
# a123.consultar_disciplinas()
