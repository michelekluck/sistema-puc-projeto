listaEstudantes = []
continuarMenuPrincipal = True
while continuarMenuPrincipal:
    print("-"*20, "MENU PRINCIPAL","-"*20)
    print("\n(1) Gerenciar estudantes. \n(2) Gerenciar Professores. \n(3) Gerenciar disciplinas. \n(4) Gerenciar turmas. \n(5) Gerenciar matriculas. \n(6) Sair.")
    
    opcaoMenuPrincipal = ""
    
    respostaPrincipal = int(input("Informe a opção desejada: "))
    
    #ESTUDANTES <<<<<
    if respostaPrincipal == 1:
        opcaoMenuPrincipal = "ESTUDANTES"
        
    # PROFESSORES <<<<<<<<
    elif respostaPrincipal == 2:
        opcaoMenuPrincipal = "PROFESSORES"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    
    # DISCIPLINAS <<<<<<<
    elif respostaPrincipal == 3:
        opcaoMenuPrincipal = "DISCIPLINAS"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    
    # TURMAS <<<<<<<<<
    elif respostaPrincipal == 4:
        opcaoMenuPrincipal = "TURMAS"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    
    # MATRICULAS <<<<<<<,
    elif respostaPrincipal == 5:
        opcaoMenuPrincipal = "MATRICULAS"
        print(f"\n{opcaoMenuPrincipal}\nEM DESENVOLVIMENTO\n")
        continue
    
    # SAIR <<<<<<<<
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
        
        #INCLUSÃO <<<<<<<<<<<<<<
        if respostaOperacoes == 1:
            print("="*5, "INCLUSÃO", "="*5)
            # o usuario navegou pelas opções ESTUDANTES -> INCLUIR até chegar no código abaixo:
            if opcaoMenuPrincipal == "ESTUDANTES":
                nomeEstudante = str(input("Informe o nome do estudante: "))
                codigoEstudante = int(input("Digite o codigo do estudante: "))
                cpfEstudante = input("Digite o CPF: ")
                dicionarioEstudante = {
                    "nome": nomeEstudante,
                    "codigo": codigoEstudante,
                    "cpf": cpfEstudante
                }
                listaEstudantes.append(dicionarioEstudante)
                input("\nPressione ENTER para continuar.\n") 
            else:
                print("\nEM DESENVOLVIMENTO\n")
                
        # LISTAGEM <<<<<<<<<<
        elif respostaOperacoes == 2:
            print("="*5, "LISTAGEM", "="*5)
            # o usuario navegou pelas opções ESTUDANTES -> LISTAR até chegar no código abaixo:
            if opcaoMenuPrincipal == "ESTUDANTES":
                if len(listaEstudantes) == 0:
                    print("\nNao há estudantes cadastrados\n")
                for estudante in listaEstudantes:
                    print(estudante)
            input("\nPressione ENTER para continuar.\n")
            
        # ATUALIZAÇÃO <<<<<<<<<<<<<<<
        elif respostaOperacoes == 3:
            print("="*5,"ATUALIZAÇÃO","="*5)
            editarEstudante = int(input("Qual código de estudante você deseja editar? "))
            estudanteEditado = None
            for estudante in listaEstudantes:
                if estudante["codigo"] == editarEstudante:
                    estudanteEditado = estudante
                    break
            if estudanteEditado is None:
                print(f"Código {editarEstudante} não encontrado.")
            else:
                estudanteEditado["codigo"] = int(input("Digite o novo código: "))
                estudanteEditado["nome"] = input("Digite o novo nome do estudante: ")
                estudanteEditado["cpf"] = input("Digite o novo CPF: ")
                print(f"Código {editarEstudante} atualizado.") 
            
        #EXCLUSÃO<<<<<<<<<
        elif respostaOperacoes == 4:
            print("="*5, "EXCLUSÃO", "="*5)
            excluirCodigo = int(input("\nQual é o código que deseja excluir? "))
            estudanteRemovido = None
            for estudante in listaEstudantes:
                if estudante["codigo"] == excluirCodigo:
                    estudanteRemovido = estudante
                    print(f"\nEstudante com código {excluirCodigo} removido. \n")
                    break
            if estudanteRemovido is None:
                print(f"\nEstudante com codigo {excluirCodigo} não encontrado.\n")
            else:
                listaEstudantes.remove(estudanteRemovido)

        elif respostaOperacoes == 5:
            # VOLTAR AO MENU PRINCIPAL <<<<<<<<<<<<<
            print("\nVoltar ao menu principal\n")
    
        else:
            print("\nOpção Inválida! Digite uma opção válida.\n")

print("Finalizando aplicação...")