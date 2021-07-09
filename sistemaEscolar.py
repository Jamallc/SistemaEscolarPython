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
            print('Mat | Aluno | N1 | N2 | Média | Resultado')
            print('-----------------------------------------')
            for aluno in self.alunos:
                media = (float(aluno[1]) + float(aluno[2]))/2
                aprovacao = ''
                if media > 5:
                    aprovacao = "Aprovado"
                else:
                    aprovacao = "Reprovado"
                print(
                    f'{aluno[0].matricula} | {aluno[0].nome} | {aluno[1]} | {aluno[2]} | {media} | {aprovacao}')
                print('-----------------------------------------')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        self.matricula = matricula
        self.disciplinas = []
        super().__init__(nome, idade)

    def cadastrar_disciplinas(self, disciplina, nota1, nota2):
        self.disciplinas.append([disciplina, nota1, nota2])

    def consultar_disciplinas(self):
        if(len(self.disciplinas) == 0):
            print('Aluno sem disciplinas matriculadas')
        else:
            print('Matriculado em:')
            for i in self.disciplinas:
                print(
                    f'| {i[0].codigo} | {i[0].nomeDisciplina} | Nota 1: {i[1]} | Nota 2: {i[2]} |')
                print('---------------------------------------------')


def menu():
    continuar = 1

    while continuar:
        continuar = input("0. Sair\n" +
                        "1. Exibir relatório de disciplinas\n" +
                        "2. Inserir aluno\n" +
                        "3. Inserir Disciplina \n" +
                        "4. Matricular aluno em uma disciplina\n" +
                        "5. Ver matérias de um aluno\n")
        if continuar == '1':
            exibirRelatorio()
        elif continuar == '2':
            inserirAluno()
        elif continuar == '3':
            inserirDisciplina()
        elif continuar == '4':
            MatricularAluno()
        elif continuar == '5':
            exibirRelatorioIndividual()
        elif continuar == '0':
            print("Encerrando programa")
            return
        else:
            print("Opção inválida")


RelatorioDisciplinas = []
AlunosMatriculados = []


def exibirRelatorio():
    if(len(RelatorioDisciplinas) == 0):
        print("Nenhuma disciplina cadastrada!")
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
    cont = 0
    for d in RelatorioDisciplinas:
        cont += 1
        if disciplina == d[0]:
            print(
                f"\033[1m Disciplina {cont} \033[0m - {d[2].nomeDisciplina} - Código {d[2].codigo}")
            print(d[2].relatorio())


def exibirRelatorioIndividual():
    if(len(RelatorioDisciplinas) == 0):
        print("Nenhuma disciplina cadastrada!")
        return
    if(len(AlunosMatriculados) == 0):
        print("Nenhum aluno cadastrado!")
        return
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
    for a in AlunosMatriculados:
        if aluno == a[0]:
            print(a[3].consultar_disciplinas())


def inserirAluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno (somente números): ")
    q = 1
    while q == 1:
        error = []
        if not idade.isdigit():
            idade = input("Digite a idade do aluno (somente números): ")
            error.append(idade)
        if len(error) == 0:
            q = 0
    f = 1
    while f == 1:
        matricula = 'a'+input("Digite a matrícula do aluno: ")
        erro = 0
        for aluno in AlunosMatriculados:
            if matricula == aluno[0]:
                erro = 1
        if erro != 0:
            print("Ja existe um aluno com essa matrícula: ", matricula)
        else:
            AlunosMatriculados.append([matricula, nome, idade, matricula])
            for aluno in AlunosMatriculados:
                if matricula == aluno[0]:
                    aluno[3] = Aluno(nome, idade, matricula)
            f = 0


def inserirDisciplina():
    nomeDisciplina = input("Nome da disciplina: ")
    for disciplina in RelatorioDisciplinas:
        if nomeDisciplina in disciplina[1]:
            print("Disciplina já cadastrada")
            return
    c = 1
    while c == 1:
        erro = []
        codigo = 'd'+input("Código da disciplina: ")
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


def MatricularAluno():
    if(len(RelatorioDisciplinas) == 0):
        print("Nenhuma disciplina cadastrada!")
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
        conf = 0
        aluno = input("Digite a matrícula do aluno: ")
        for alun in AlunosMatriculados:
            if aluno == alun[0]:
                for dis in alun[3].disciplinas:
                    if dis[0].codigo == disciplina:
                        conf = 1
                if conf == 0:
                    al = 0
                    erro = []
                    break
                else:
                    print("Aluno já matriculado nessa disciplina!")
                    return
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
            # a[3].consultar_disciplinas()

    for d in RelatorioDisciplinas:
        if disciplina == d[0]:
            for a in AlunosMatriculados:
                if aluno == a[0]:
                    al = a[3]
            d[2].associar_aluno(al, nota1, nota2)
            # d[2].relatorio()


menu()
