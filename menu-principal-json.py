import json

listaEstudantes = []

def menuPrincipal():
    while True:
        print("-"*20, "MENU PRINCIPAL","-"*20)
        print("\n(1) Gerenciar estudantes. \n(2) Gerenciar Professores. \n(3) Gerenciar disciplinas. \n(4) Gerenciar turmas. \n(5) Gerenciar matriculas. \n(6) Sair.")
        opcao = opcaoEscolhida()
        opcoes = {
            1: gerenciarEstudantes,
            2: gerenciarProfessores,
            3: gerenciarDisciplinas,
            4: gerenciarTurmas,
            5: gerenciarMatriculas,
        }
        if opcao in opcoes:
            opcoes[opcao]()
        elif opcao == 6:
            print("\nSAINDO\n")
            break
        else:
            print("Opção Inválida")

def opcaoEscolhida():
    opcao = int(input("Informe a opção desejada "))
    return opcao

def enterParaContinuar():
    input("Pressione ENTER para continuar")
    
def gerenciarEstudantes():
    while True:
        opcao = menuOperacoes("ESTUDANTES")
        opcoes = {
            1: incluirEstudante,
            2: listarEstudantes,
            3: atualizarEstudante,
            4: excluirEstudante,
        }
        if opcao in opcoes:
            opcoes[opcao]()
        elif opcao == 5:
            break
        else:
            print("Opção Inválida")
            enterParaContinuar()

def menuOperacoes(escolhaMenuPrincipal):
    print("*"*4, f"[{escolhaMenuPrincipal}]", "MENU DE OPERAÇÕES","*"*4)
    print("\n(1) Incluir. \n(2) Listar. \n(3) Atualizar \n(4) Excluir. \n(5) Voltar ao menu principal.")
    return opcaoEscolhida()


def incluirEstudante():
        print("="*5, "INCLUSÃO", "="*5)
        nomeEstudante = str(input("Informe o nome do estudante: "))
        codigoEstudante = int(input("Digite o codigo do estudante: "))
        cpfEstudante = input("Digite o CPF: ")
        dicionarioEstudante = {
        "nome": nomeEstudante,
        "codigo": codigoEstudante,
        "cpf": cpfEstudante
        }
        listaEstudantes.append(dicionarioEstudante)
        salvarListaEstudante()
        enterParaContinuar()
        
def listarEstudantes():
    print("="*5, "LISTAGEM", "="*5)
    if len(listaEstudantes) == 0:
        print("\n Não há estudantes cadastrados\n")
    for estudante in listaEstudantes:
        print(estudante)
    enterParaContinuar()

def atualizarEstudante():
    print("="*5,"ATUALIZAÇÃO","="*5)
    estudanteASerEditado = int(input("Qual código de estudante você deseja editar? "))
    estudanteEditado = None
    for estudante in listaEstudantes:
        if estudante["codigo"] == estudanteASerEditado:
            estudanteEditado = estudante
            break
    if estudanteEditado is None:
        print(f"Código {estudanteASerEditado} não encontrado")
    else:
        estudanteEditado["codigo"] = int(input("Digite o novo código: "))
        estudanteEditado["nome"] = input("Digite o novo nome do estudante: ")
        estudanteEditado["cpf"] = input("Digite o novo CPF: ")
        print(f"Código {estudanteASerEditado} atualizado.")

def excluirEstudante():
    print("="*5, "EXCLUSÃO", "="*5)
    codigoASerExcluido = int(input("\nQual é o código que deseja excluir? "))
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

def gerenciarProfessores():
    print("\nEM DESENVOLVIMENT0\n")
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

def salvarListaEstudante():
    with open("estudantes.json", "w", encoding="utf-8") as arquivo:
        json.dump(listaEstudantes, arquivo, ensure_ascii=False)
    
menuPrincipal()