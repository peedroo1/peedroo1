#Função para incluir um estudante na lista de estudantes
def incluir_estudante(lista):
    nome = input("Digite o nome do estudante: ")  #Solicita o nome do estudante
    if nome in lista:  #Verifica se o nome já está na lista
        print("Erro: Este estudante já está cadastrado.")
    else:
        lista.append(nome)  #Adiciona o nome do estudante à lista
        print("Estudante", nome, "incluído com sucesso.")

#Função para listar os estudantes
def listar_estudantes(lista):
    if len(lista) == 0:  #Verifica se a lista dos estudantes está vazia
        print("Não há estudantes cadastrados.")  #Se a lista estiver vazia, imprime a mensagem
    else:
        print("Lista de estudantes:")  #Imprime o nome da lista
        for estudante in lista:
            print("-" + estudante)  #Imprime o nome do estudante

#Função para incluir um professor na lista de professores
def incluir_professor(lista):
    codigo = input("Digite o código do professor: ")
    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")
    lista.append({"Código": codigo, "Nome": nome, "CPF": cpf})
    print("Professor cadastrado com sucesso.")

#Função para listar os professores
def listar_professores(lista):
    if len(lista) == 0:
        print("Não há professores cadastrados.")
    else:
        print("Lista de professores:")
        for professor in lista:
            print("- Código:", professor["Código"])
            print("  Nome:", professor["Nome"])
            print("  CPF:", professor["CPF"])

#Função para incluir uma disciplina na lista de disciplinas
def incluir_disciplina(lista):
    codigo = input("Digite o código da disciplina: ")
    nome = input("Digite o nome da disciplina: ")
    lista.append({"Código": codigo, "Nome": nome})
    print("Disciplina cadastrada com sucesso.")

#Função para listar as disciplinas
def listar_disciplinas(lista):
    if len(lista) == 0:
        print("Não há disciplinas cadastradas.")
    else:
        print("Lista de disciplinas:")
        for disciplina in lista:
            print("- Código:", disciplina["Código"])
            print("  Nome:", disciplina["Nome"])

#Função para incluir uma turma na lista de turmas
def incluir_turma(lista_turmas, lista_professores, lista_disciplinas):
    codigo = input("Digite o código da turma: ")
    codigo_professor = input("Digite o código do professor: ")
    codigo_disciplina = input("Digite o código da disciplina: ")

    codigo_professor = int(codigo_professor) if codigo_professor.isdigit() else codigo_professor
    codigo_disciplina = int(codigo_disciplina) if codigo_disciplina.isdigit() else codigo_disciplina

    #Verifica se o código da turma já existe
    for turma in lista_turmas:
        if turma["Código"] == codigo:
            print("Erro: Este código de turma já está cadastrado.")
            return

    #Verifica se o código do professor existe na lista de professores
    professor_existente = False
    for professor in lista_professores:
        if professor["Código"] == codigo_professor:
            professor_existente = True
            break
    if not professor_existente:
        print("Erro: O código do professor não existe.")
        return

    #Verifica se o código da disciplina existe na lista de disciplinas
    disciplina_existente = False
    for disciplina in lista_disciplinas:
        if disciplina["Código"] == codigo_disciplina:
            disciplina_existente = True
            break
    if not disciplina_existente:
        print("Erro: O código da disciplina não existe.")
        return

    #Adiciona a turma à lista de turmas
    lista_turmas.append({"Código": codigo, "Código do Professor": codigo_professor, "Código da Disciplina": codigo_disciplina})
    print("Turma cadastrada com sucesso.")

#Função para listar todas as turmas
def listar_turmas(lista_turmas):
    if len(lista_turmas) == 0:
        print("Não há turmas cadastradas.")
    else:
        print("Lista de turmas:")
        for turma in lista_turmas:
            print("- Código:", turma["Código"])
            print("  Código do Professor:", turma["Código do Professor"])
            print("  Código da Disciplina:", turma["Código da Disciplina"])

#Função para incluir uma matrícula na lista de matrículas
def incluir_matricula(lista_matriculas, lista_turmas, lista_estudantes):
    codigo_turma = input("Digite o código da turma: ")
    codigo_estudante = input("Digite o código do estudante: ")

    #Verifica se o código da turma existe na lista de turmas
    turma_existente = False
    for turma in lista_turmas:
        if turma["Código"] == codigo_turma:
            turma_existente = True
            break
    if not turma_existente:
        print("Erro: O código da turma não existe.")
        return

    #Verifica se o código do estudante existe na lista de estudantes
    estudante_existente = False
    for estudante in lista_estudantes:
        if estudante["Código"] == codigo_estudante:
            estudante_existente = True
            break
    if not estudante_existente:
        print("Erro: O código do estudante não existe.")
        return

    #Adiciona a matrícula à lista de matrículas
    lista_matriculas.append({"Código da Turma": codigo_turma, "Código do Estudante": codigo_estudante})
    print("Matrícula realizada com sucesso.")

#Função para listar as matrículas
def listar_matriculas(lista_matriculas):
    if len(lista_matriculas) == 0:
        print("Não há matrículas cadastradas.")
    else:
        print("Lista de matrículas:")
        for matricula in lista_matriculas:
            print("- Código da Turma:", matricula["Código da Turma"])
            print("  Código do Estudante:", matricula["Código do Estudante"])

#Função para exibir o menu principal
def menu_principal():
    print("** MENU PRINCIPAL **")
    print("1 - Incluir estudante")
    print("2 - Listar estudantes")
    print("3 - Incluir professor")
    print("4 - Listar professores")
    print("5 - Incluir disciplina")
    print("6 - Listar disciplinas")
    print("7 - Incluir turma")
    print("8 - Listar turmas")
    print("9 - Incluir matrícula")
    print("10 - Listar matrículas")
    print("11 - Sair")

#Função principal
def main():
    lista_estudantes = []  #Lista que armazena os estudantes
    lista_professores = []  #Lista que armazena os professores
    lista_disciplinas = []  #Lista que armazena as disciplinas
    lista_turmas = []  #Lista que armazena as turmas
    lista_matriculas = []  #Lista que armazena as matrículas

    while True:  #Loop para sempre apresentar o menu
        menu_principal()  #Mostra o menu principal
        opcao = input("Digite o número da opção desejada: ")  #Pede que o usuário digite uma das opções apresentadas no menu

        if opcao == "1":  #Se a opção escolhida for "Incluir estudante"
            incluir_estudante(lista_estudantes)  #Chama a função para incluir um estudante
        elif opcao == "2":  #Se a opção escolhida for "Listar estudantes"
            listar_estudantes(lista_estudantes)  #Chama a função para listar os estudantes
        elif opcao == "3":  #Se a opção escolhida for "Incluir professor"
            incluir_professor(lista_professores)  #Chama a função para incluir um professor
        elif opcao == "4":  #Se a opção escolhida for "Listar professores"
            listar_professores(lista_professores)  #Chama a função para listar os professores
        elif opcao == "5":  #Se a opção escolhida for "Incluir disciplina"
            incluir_disciplina(lista_disciplinas)  #Chama a função para incluir uma disciplina
        elif opcao == "6":  #Se a opção escolhida for "Listar disciplinas"
            listar_disciplinas(lista_disciplinas)  #Chama a função para listar as disciplinas
        elif opcao == "7":  #Se a opção escolhida for "Incluir turma"
            incluir_turma(lista_turmas, lista_professores, lista_disciplinas)  #Chama a função para incluir uma turma
        elif opcao == "8":  #Se a opção escolhida for "Listar turmas"
            listar_turmas(lista_turmas)  #Chama a função para listar as turmas
        elif opcao == "9":  #Se a opção escolhida for "Incluir matrícula"
            incluir_matricula(lista_matriculas, lista_turmas, lista_estudantes)  #Chama a função para incluir uma matrícula
        elif opcao == "10":  #Se a opção escolhida for "Listar matrículas"
            listar_matriculas(lista_matriculas)  #Chama a função para listar as matrículas
        elif opcao == "11":  #Se a opção escolhida for "Sair"
            print("Saindo do programa...")  #Imprime uma mensagem de despedida
            break  #Sai do loop e encerra o programa
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")  #Mensagem de erro se a opção for inválida

if __name__ == "__main__":
    main()  #Chama a função principal quando o script é executado diretamente
