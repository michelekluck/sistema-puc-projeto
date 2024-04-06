listaEstudantes = []
continuarMenuPrincipal = True
while continuarMenuPrincipal:
    print("-"*20, "MENU PRINCIPAL","-"*20)
    print("\n(1) Gerenciar estudantes. \n(2) Gerenciar Professores. \n(3) Gerenciar disciplinas. \n(4) Gerenciar turmas. \n(5) Gerenciar matriculas. \n(6) Sair.")
    
    opcaoMenuPrincipal = ""
    
    respostaPrincipal = int(input("Informe a opção desejada: "))
    if respostaPrincipal == 1:
        opcaoMenuPrincipal = "ESTUDANTES"
    elif respostaPrincipal == 2:
        opcaoMenuPrincipal = "PROFESSORES"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    elif respostaPrincipal == 3:
        opcaoMenuPrincipal = "DISCIPLINAS"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    elif respostaPrincipal == 4:
        opcaoMenuPrincipal = "TURMAS"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    elif respostaPrincipal == 5:
        opcaoMenuPrincipal = "MATRICULAS"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    elif respostaPrincipal == 6:
        print("-"*20,"[SAINDO]","-"*20)
        break
    else:
        print("\nOpção Inválida! Digite uma opção válida:\n")
        continue
        
    respostaOperacoes = 0
    while respostaOperacoes != 5:
        print("*"*4, f"[{opcaoMenuPrincipal}]", "MENU DE OPERAÇÕES","*"*4)
        
        print("\n(1) Incluir. \n(2) Listar. \n(3) Atualizar \n(4) Excluir. \n(5) Voltar ao menu principal.")

        respostaOperacoes = int(input("Informe a ação desejada: "))
        if respostaOperacoes == 1:
            print("="*5, "INCLUSÃO", "="*5)
            if opcaoMenuPrincipal == "ESTUDANTES":
                nomeEstudante = str(input("Informe o nome do estudante: "))
                listaEstudantes.append(nomeEstudante)
                input("Pressione ENTER para continuar.")
            else:
                print("\nEM DESENVOLVIMENTO\n")
        elif respostaOperacoes == 2:
            print("="*5, "LISTAGEM", "="*5)
            if opcaoMenuPrincipal == "ESTUDANTES":
                if len(listaEstudantes) == 0:
                    print("Nao há estudantes cadastrados")
                for nomeEstudante in listaEstudantes:
                    print("-", nomeEstudante)
            input("Pressione ENTER para continuar.")
        elif respostaOperacoes == 3:
            print("="*5,"ATUALIZAÇÃO","="*5)
            print("\nEM DESENVOLVIMENTO\n")
        elif respostaOperacoes == 4:
            print("="*5, "EXCLUSÃO", "="*5)
            print("\nEM DESENVOLVIMENTO\n")
        elif respostaOperacoes == 5:
            print("\nVoltar ao menu principal\n")
        else:
            print("\nOpção Inválida! Digite uma opção válida.\n")

print("Finalizando aplicação...")