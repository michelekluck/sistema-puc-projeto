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
    elif respostaPrincipal == 3:
        opcaoMenuPrincipal = "DISCIPLINAS"
    elif respostaPrincipal == 4:
        opcaoMenuPrincipal = "TURMAS"
    elif respostaPrincipal == 5:
        opcaoMenuPrincipal = "MATRICULAS"
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
            print("="*5, "INCLUINDO", "="*5)
        elif respostaOperacoes == 2:
            print("="*5, "LISTANDO", "="*5)
        elif respostaOperacoes == 3:
            print("="*5,"ATUALIZAÇÃO","="*5)
        elif respostaOperacoes == 4:
            print("="*5, "EXCLUINDO", "="*5)
        elif respostaOperacoes == 5:
            print("\nVoltar ao menu principal\n")
        else:
            print("\nOpção Inválida! Digite uma opção válida.\n")

print("Finalizando aplicação...")