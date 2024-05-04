def gerenciar():
    opcao = opcaoEscolhida()
    if opcao == 1:
        while True:
            opcao = menuOperacoes("ESTUDANTES") #variavel
            if opcao == 1:
                incluir(listaEstudantes, "estudantes.json", grupo="Estudante")
            elif opcao == 6:
                print("\nSAINDO\n")
                break
            else:
                print("Opção Inválida")

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
    
def incluirTurmas(lista, nome_arquivo):
    print("="*5, "INCLUSÃO", "="*5)
    lista = lerListaDoJson(nome_arquivo)
    turma = int(input("Digite o codigo da turma: "))
    professor = int(input("Digite o codigo do professor: "))
    disciplina = int(input("Digite o codigo da disciplina: "))
    dicionarioGrupo = {
        "turma": turma,
        "professor": professor,
        "disciplina" : disciplina,
    }  
    lista.append(dicionarioGrupo)
    print(f"\nTurma {turma} adicionada.")
    salvarListaemJson(lista, nome_arquivo)
    enterParaContinuar()
    
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