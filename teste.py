def atualizarEstudante():
    print("="*5,"ATUALIZAÇÃO","="*5)
    listaEstudantes = lerListaDoJson("estudantes.json")
    estudanteASerEditado = input("Qual código de estudante você deseja editar? ")
    estudanteEditado = None
    for estudante in listaEstudantes:
        if estudante["codigo"] == estudanteASerEditado:
            estudanteEditado = estudante
            break
    if estudanteEditado is None:
        print(f"Código {estudanteASerEditado} não encontrado")
    else:
        estudanteEditado["codigo"] = input("Digite o novo código: ")
        estudanteEditado["nome"] = input("Digite o novo nome do estudante: ")
        estudanteEditado["cpf"] = input("Digite o novo CPF: ")
        print(f"\nEstudante com código {estudanteASerEditado} atualizado.\n")
        salvarListaemJson(listaEstudantes, "estudantes.json")
        enterParaContinuar()
        
def incluirProfessoresEstudantes(lista, nome_arquivo, grupo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson (nome_arquivo)
    nome = input(f"Informe o nome do {grupo}: ")
    codigo = int(input(f"Digite o codigo do {grupo}: "))
    cpf = input(f"Digite o CPF do {grupo}: ")
    dicionarioGrupo = {
    "nome": nome,
    "codigo": codigo,
    "cpf": cpf
    } 
    lista.append(dicionarioGrupo) #variavel
    print(f"\n{grupo} {nome} adicionado.\n")
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar() 
    

    
def excluirEstudante():
    print("="*5, "EXCLUSÃO", "="*5)
    listaEstudantes = lerListaDoJson("estudantes.json")
    codigoASerExcluido = input("\nQual é o código que deseja excluir? ")
    estudanteRemovido = None
    for estudante in listaEstudantes:
        if estudante["codigo"] == codigoASerExcluido:
            estudanteRemovido = estudante
            print(f"\nEstudante com código {codigoASerExcluido} removido.\n")
            break
    if estudanteRemovido is None:
        print(f"\nEstudante com codigo {codigoASerExcluido} não encontrado\n")
    else:
        listaEstudantes.remove(estudanteRemovido)
    salvarListaemJson(listaEstudantes, "estudantes.json")
    enterParaContinuar()
    
# FUNÇÃO INCLUIR TURMAS <<<<<<    
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
    
# INCLUIR PROFESSORES E ESTUDANTES
def incluirProfessoresEstudantes(lista, nome_arquivo, grupo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson (nome_arquivo)
    nome = input(f"Informe o nome do {grupo}: ")
    codigo = int(input(f"Digite o codigo do {grupo}: "))
    cpf = input(f"Digite o CPF do {grupo}: ")
    dicionarioGrupo = {
    "nome": nome,
    "codigo": codigo,
    "cpf": cpf
    } 
    lista.append(dicionarioGrupo) #variavel
    print(f"\n{grupo} {nome} adicionado.\n")
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()
    
    
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
        print(f"Disciplina com codigo {codigoASerEditado} não encontrada.")
    else:
        codigoEditado["codigo"] = int(input("Digite o novo código: "))
        codigoEditado["disciplina"] = input("Digite o novo nome de disciplina: ")
        print(f"\nDisciplina com {codigoASerEditado} atualizada.\n")
        salvarListaemJson(lista, nome_arquivo)
        enterParaContinuar()