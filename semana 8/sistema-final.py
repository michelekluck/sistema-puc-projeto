import json

listaEstudantes = []
listaProfessores = []

def menuPrincipal():
    while True:
        print("-"*20, "MENU PRINCIPAL","-"*20)
        print("\n(1) Gerenciar Estudantes. \n(2) Gerenciar Professores. \n(3) Gerenciar disciplinas. \n(4) Gerenciar turmas. \n(5) Gerenciar matriculas. \n(6) Sair.")
        gerenciar()

def opcaoEscolhida():
    opcao = int(input("Informe a opção desejada "))
    return opcao

def enterParaContinuar():
    input("Pressione ENTER para continuar")

def gerenciar(grupo, ):
    opcao = opcaoEscolhida()
    if opcao == 1:
        while True:
            opcao = menuOperacoes(f"{grupo}") #variavel
            if opcao == 1:
                incluir(listaEstudantes, "estudantes.json", grupo="Estudante")
            elif opcao == 5:
                break
            else:
                print("Opção Inválida")
    elif opcao == 2:
        while True:
            opcao = menuOperacoes("PROFESSORES") #variavel
            if opcao == 1:
                incluir(listaProfessores, "professores.json", grupo="Professor(a)")
            elif opcao == 5:
                break
            else:
                print("Opção Inválida")       
    enterParaContinuar()       
            
# FUNÇÃO INCLUIR<<<<<<<<
def incluir(lista, nome_arquivo, grupo):
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

def menuOperacoes(escolhaMenuPrincipal):
    print("*"*4, f"[{escolhaMenuPrincipal}]", "MENU DE OPERAÇÕES","*"*4)
    print("\n(1) Incluir. \n(2) Listar. \n(3) Atualizar \n(4) Excluir. \n(5) Voltar ao menu principal.")
    return opcaoEscolhida()


def incluirEstudante():
        print("="*5, "INCLUSÃO", "="*5)
        listaEstudantes = lerListaDoJson("estudantes.json")
        nomeEstudante = input("Informe o nome do estudante: ")
        codigoEstudante = input("Digite o codigo do estudante: ")
        cpfEstudante = input("Digite o CPF: ")
        dicionarioEstudante = {
        "nome": nomeEstudante,
        "codigo": codigoEstudante,
        "cpf": cpfEstudante
        }
        listaEstudantes.append(dicionarioEstudante)
        print(f"\nEstudante {nomeEstudante} adicionado.\n")
        salvarListaemJson(listaEstudantes, "estudantes.json")
        enterParaContinuar()

def listarEstudantes():
    print("="*5, "LISTAGEM", "="*5)
    listaEstudantes = lerListaDoJson("estudantes.json")
    if len(listaEstudantes) == 0:
        print("\n Não há estudantes cadastrados\n")
    for estudante in listaEstudantes:
        print(estudante)
    enterParaContinuar()

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
    
def gerenciarDisciplinas():
    print("\nEM DESENVOLVIMENT0\n")   
    enterParaContinuar() 

def gerenciarTurmas():
    print("\nEM DESENVOLVIMENT0\n")   
    enterParaContinuar()

def gerenciarMatriculas():
    print("\nEM DESENVOLVIMENT0\n") 
    enterParaContinuar()

def salvarListaemJson(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)
        
def lerListaDoJson(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dadosLidos = json.load(arquivo)
        return dadosLidos
    except:
        return[]
        
menuPrincipal()