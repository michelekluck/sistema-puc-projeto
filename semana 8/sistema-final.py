import json

listaEstudantes = []
listaProfessores = []
listaDisciplinas = []
listaTurmas = []
listaMatriculas = []

# MENU PRINCIPAL
def menuPrincipal():
    while True:
        print("-"*20, "MENU PRINCIPAL","-"*20)
        print("\n(1) Gerenciar Estudantes. \n(2) Gerenciar Professores. \n(3) Gerenciar disciplinas. \n(4) Gerenciar turmas. \n(5) Gerenciar matriculas. \n(6) Sair.")
        gerenciar()
        
# OPÇÃO ESCOLHIDA
def opcaoEscolhida():
    opcao = int(input("Informe a opção desejada "))
    return opcao

# MENU DE OPERAÇÕES    
def menuOperacoes(escolhaMenuPrincipal):
    print("*"*4, f"[{escolhaMenuPrincipal}]", "MENU DE OPERAÇÕES","*"*4)
    print("\n(1) Incluir. \n(2) Listar. \n(3) Atualizar \n(4) Excluir. \n(5) Voltar ao menu principal.")
    return opcaoEscolhida()

# ENTER PARA CONTINUAR
def enterParaContinuar():
    input("Pressione ENTER para continuar")

# FUNÇÃO GERENCIAR
def gerenciar():
    opcao = opcaoEscolhida()
    # ESTUDANTES
    if opcao == 1:
        while True:
            opcao = menuOperacoes("ESTUDANTES")
            if opcao == 1:
                incluirProfessoresEstudantes(listaEstudantes, "estudantes.json", grupo="Estudante")
            elif opcao == 2:
                listarTodos(listaEstudantes, "estudantes.json", grupo="estudantes")
            elif opcao == 3:
                atualizarProfessorEstudante(listaEstudantes, "estudantes.json", grupo="estudante")
            elif opcao == 4:
                excluirProfessoresEstudantesDisciplinas(listaEstudantes, "estudantes.json", grupo="Estudante")
            elif opcao == 5:
                menuPrincipal()
            elif opcao == 6:
                print("\nSAINDO\n")
                break
            else:
                print("Opção Inválida")
    # PROFESSORES
    if opcao == 2:
        while True:
            opcao = menuOperacoes("PROFESSORES")
            if opcao == 1:
                incluirProfessoresEstudantes(listaProfessores, "professores.json", grupo="Professor(a)")
            elif opcao == 2:
                listarTodos(listaProfessores, "professores.json", grupo="professores")
            elif opcao == 3:
                atualizarProfessorEstudante(listaProfessores, "professores.json", grupo="professor(a)")
            elif opcao == 4:
                excluirProfessoresEstudantesDisciplinas(listaProfessores, "professores.json", grupo="Professor(a)")
            elif opcao == 5:
                menuPrincipal()
            elif opcao == 6:
                print("\nSAINDO\n")
                break
            else:
                print("Opção Inválida")
    #DISCIPLINAS
    if opcao == 3:
        while True:
            opcao = menuOperacoes("DISCIPLINAS")
            if opcao == 1:
                incluirDisciplinas(listaDisciplinas, "disciplinas.json")
            elif opcao == 2:
                listarTodos(listaDisciplinas, "disciplinas.json", grupo="disciplinas")
            elif opcao == 3:
                atualizarDisciplina(listaDisciplinas, "disciplinas.json")
            elif opcao == 4:
                excluirProfessoresEstudantesDisciplinas(listaDisciplinas, "disciplinas.json", grupo="Disciplina")
            elif opcao == 5:
                menuPrincipal()
            elif opcao == 6:
                print("\nSAINDO\n")
                break
            else:
                print("Opção Inválida")
    # TURMAS
    if opcao == 4:
        while True:
            opcao = menuOperacoes("TURMAS")     
            if opcao == 1:
                incluirTurmas(listaTurmas, "turmas.json")
            elif opcao == 2:
                listarTodos(listaTurmas, "turmas.json", grupo="turmas")
            elif opcao == 3:
                atualizarTurma(listaTurmas, "turmas.json")
            elif opcao == 4:
                excluirTurma(listaTurmas, "turmas.json")
            elif opcao == 5:
                menuPrincipal()   
            elif opcao == 6:
                print("\nSAINDO\n")
                break
            else:
                print("Opção Inválida")
    # MATRICULAS
    if opcao == 5:
        while True:
            opcao = menuOperacoes("MATRICULAS")
            if opcao == 1:
                incluirMatriculas(listaMatriculas, "matriculas.json")
            elif opcao == 2:
                listarTodos(listaMatriculas, "matriculas.json", grupo="matriculas")
            elif opcao == 3:
                atualizarMatricula(listaMatriculas, "matriculas.json")
            elif opcao == 4:
                excluirMatricula(listaMatriculas, "matriculas.json")
            elif opcao == 5:
                menuPrincipal()
            elif opcao == 6:
                print("\nSAINDO\n")
                break
            else:
                print("Opção Inválida")         
    enterParaContinuar()

# INCLUIR PROFESSORES E ESTUDANTES
def incluirProfessoresEstudantes(lista, nome_arquivo, grupo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson (nome_arquivo)
    codigoASerAdicionado = int(input(f"Digite o codigo do {grupo}: "))
    codigoJaAdicionado = None
    for codigo in lista:
        if codigo["codigo"] == codigoASerAdicionado:
            codigoJaAdicionado = codigo
            print(f"\n{grupo} com código {codigoASerAdicionado} já existe, tente novamente.\n")
    if codigoJaAdicionado is None:
        nome = input(f"Informe o nome do {grupo}: ")
        cpf = input(f"Digite o CPF do {grupo}: ")
        dicionarioGrupo = {
            "codigo": codigoASerAdicionado,
            "nome": nome,
            "cpf": cpf
        }
        print(f"\n{grupo} {nome} adicionado.\n")
        lista.append(dicionarioGrupo)
        enterParaContinuar()
    salvarListaemJson(lista, nome_arquivo)
        
                 
# LISTAR TODOS 
def listarTodos(lista, nome_arquivo, grupo):
    print("="*5, "LISTAGEM", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    if len(lista) == 0:
        print(f"\n Não há {grupo} cadastrados\n")
    print(f"\nLista de {grupo}:\n")
    for dado in lista:
        print(dado)
    enterParaContinuar()

# ATUALIZAR PROFESSOR E ESTUDANTE   
def atualizarProfessorEstudante(lista, nome_arquivo, grupo):
    print("="*5,"ATUALIZAÇÃO","="*5)
    lista = lerListaDoJson(nome_arquivo)
    grupoASerEditado = int(input(f"Qual código de {grupo} você deseja editar? "))
    grupoEditado = None
    for dado in lista:
        if dado["codigo"] == grupoASerEditado:
            grupoEditado = dado
            break
    if grupoEditado is None:
        print(f"\nCódigo {grupoASerEditado} não encontrado\n")
    else:
        grupoEditado["codigo"] = int(input("Digite o novo código: "))
        grupoEditado["nome"] = input(f"Digite o novo nome do {grupo}: ")
        grupoEditado["cpf"] = input("Digite o novo CPF: ")
        print(f"\n{grupo} com código {grupoASerEditado} atualizado.\n")
        salvarListaemJson(lista, nome_arquivo)
        enterParaContinuar()

# EXCLUIR PROFESSOR ESTUDANTE E DISCIPLINA
def excluirProfessoresEstudantesDisciplinas(lista, nome_arquivo, grupo):
    print("="*5, "EXCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    codigoASerExcluido = int(input("\nQual é o código que deseja excluir? "))
    grupoRemovido = None
    for dado in lista:
        if dado["codigo"] == codigoASerExcluido:
            grupoRemovido = dado
            print(f"\n{grupo} com código {codigoASerExcluido} removido.\n")
            break
    if grupoRemovido is None:
        print(f"\n{grupo} com codigo {codigoASerExcluido} não encontrado\n")
    else:
        lista.remove(grupoRemovido)
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()

# FUNÇÃO INCLUIR DISCIPLINAS     
def incluirDisciplinas(lista, nome_arquivo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    codigoASerAdicionado = int(input(f"Digite o codigo da Disciplina: "))
    codigoJaAdicionado = None
    for codigo in lista:
        if codigo["codigo"] == codigoASerAdicionado:
            codigoJaAdicionado = codigo
            print(f"Disciplina com codigo {codigoASerAdicionado} já existe.")
            break
    if codigoJaAdicionado is None:    
        disciplina = input(f"Informe o nome da Disciplina: ")
        dicionarioGrupo = {
        "disciplina": disciplina,
        "codigo": codigoASerAdicionado 
        }
        lista.append(dicionarioGrupo)
        print(f"\nDisciplina {disciplina} adicionado.\n")
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()
    
# ATUALIZAR DISCIPLINA
def atualizarDisciplina(lista, nome_arquivo):
    print("="*5,"ATUALIZAÇÃO","="*5)
    lista = lerListaDoJson(nome_arquivo)
    codigoASerEditado = int(input("Qual codigo de disciplina que deseja editar? "))
    codigoEditado = None
    for disciplina in lista:
        if disciplina["codigo"] == codigoASerEditado:
            codigoEditado = disciplina
            break
    if codigoEditado is None:
        print(f"\nDisciplina com codigo {codigoASerEditado} não encontrada.\n")
    else:
        codigoEditado["codigo"] = int(input("Digite o novo código: "))
        codigoEditado["disciplina"] = input("Digite o novo nome de disciplina: ")
        print(f"\nDisciplina com {codigoASerEditado} atualizada.\n")
        salvarListaemJson(lista, nome_arquivo)
        enterParaContinuar()
        
# FUNÇÃO INCLUIR TURMAS    
def incluirTurmas(lista, nome_arquivo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    turmaAdicionar = int(input("Digite o codigo da turma: "))
    turmaJaAdicionada = None
    for turma in lista:
        if turma["turma"] == turmaAdicionar:
            turmaJaAdicionada = turma
            print(f"\nTurma {turmaAdicionar} já existe.")
            break
    if turmaJaAdicionada is None:
        professor = int(input("Digite o codigo do professor: "))
        disciplina = int(input("Digite o codigo da disciplina: "))       
        dicionarioGrupo = {
            "turma": turmaAdicionar,
            "professor": professor,
            "disciplina" : disciplina,
        } 
        print(f"\nTurma {turmaAdicionar} adicionada.")
        lista.append(dicionarioGrupo)
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()

# ATUALIZAR TURMA
def atualizarTurma(lista, nome_arquivo):
    print("="*5,"ATUALIZAÇÃO","="*5)
    lista = lerListaDoJson(nome_arquivo)
    turmaASerEditada = int(input("Qual turma que deseja editar? "))
    turmaEditada = None
    for turma in lista:
        if turma["turma"] == turmaASerEditada:
            turmaEditada = turma
            break
    if turmaEditada is None:
        print(f"\nTurma com código {turmaASerEditada} não encontrada.\n")
    else:
        turmaEditada["turma"] = int(input("Digite o novo código de turma: "))
        turmaEditada["professor"] = int(input("Digite o novo código de professor dessa turma: "))
        turmaEditada["disciplina"] = int(input("Digite o novo código de disciplina dessa turma: "))
        print(f"\nTurma com código {turmaASerEditada} atualizada.\n")
        salvarListaemJson(lista, nome_arquivo)
        enterParaContinuar()        

# EXCLUIR TURMA    
def excluirTurma(lista, nome_arquivo):
    print("="*5, "EXCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    turmaASerExcluida = int(input("\nQual turma que deseja excluir? "))
    turmaRemovida = None
    for turma in lista:
        if turma["turma"] == turmaASerExcluida:
            turmaRemovida = turma
            print(f"\nTurma {turmaASerExcluida} removida.")
            break
    if turmaRemovida is None:
        print(f"\nTurma {turmaASerExcluida} não encontrada.")
    else:
        lista.remove(turmaRemovida)
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()
    
# FUNÇÃO INCLUIR MATRICULA 
def incluirMatriculas(lista, nome_arquivo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    matriculaAdicionar = int(input("\nDigite o codigo da matrícula: "))
    matriculaJaAdicionada = None
    for matricula in lista:
        if matricula["matricula"] == matriculaAdicionar:
            matriculaJaAdicionada = matricula
            print(f"\nMatricula {matriculaAdicionar} já existe.\n")
            break
    if matriculaJaAdicionada is None:
        turma = int(input("Digite o codigo da turma: "))
        estudante = int(input("Digite o codigo do estudante: "))
        dicionarioMatricula = {
            "matricula": matriculaAdicionar,
            "turma": turma,
            "estudante": estudante 
        }
        lista.append(dicionarioMatricula)
        print(f"\nMatricula {matriculaAdicionar} adicionada.\n")
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()

# ATUALIZAR MATRICULA
def atualizarMatricula(lista, nome_arquivo):
    print("="*5,"ATUALIZAÇÃO","="*5)
    lista = lerListaDoJson(nome_arquivo)
    matriculaASerEditada = int(input("Qual codigo de matrícula que deseja editar? "))
    matriculaEditada = None
    for matricula in lista:
        if matricula["matricula"] == matriculaASerEditada:
            matriculaEditada = matricula
            break
    if matriculaEditada is None:
        print(f"Matrícula com código {matriculaASerEditada} não encontrada.")
    else:
        matriculaEditada["matricula"] = int(input("Digite o novo código de matŕicula: "))
        matriculaEditada["turma"] = int(input("Digite o novo código de turma: "))
        matriculaEditada["estudante"] = int(input("Digite o novo código de estudante: "))
        print(f"\nMatrícula com código {matriculaASerEditada} atualizada.\n")
        salvarListaemJson(lista, nome_arquivo)
        enterParaContinuar()
    
# EXCLUIR MATRICULA
def excluirMatricula(lista, nome_arquivo):
    print("="*5, "EXCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    matriculaASerExcluida = int(input("\nQual matrícula que deseja excluir? "))
    matriculaRemovida = None
    for matricula in lista:
        if matricula["matricula"] == matriculaASerExcluida:
            matriculaRemovida = matricula
            print(f"\nMatricula {matriculaASerExcluida} removida.\n")
    if matriculaRemovida is None:
        print(f"\nMatricula {matriculaASerExcluida} não encontrada.")
    else:
        lista.remove(matriculaRemovida)
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()    
    

# ESCREVER LISTA JSON    
def salvarListaemJson(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)

# LER LISTA JSON   
def lerListaDoJson(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dadosLidos = json.load(arquivo)
        return dadosLidos
    except:
        return[]
        
menuPrincipal()
    
  
    
    


    
        
        