print("-"*20, "MENU PRINCIPAL","-"*20)
print("\n(1) Gerenciar estudantes. \n(2) Gerenciar Professores. \n(3) Gerenciar disciplinas. \n(4) Gerenciar turmas. \n(5) Gerenciar matriculas. \n(6) Sair.")


respostaPrincipal = int(input("Informe a opção desejada: "))
if respostaPrincipal == 1:
    print("*"*4, "[ESTUDANTES]", "MENU DE OPERAÇÕES","*"*4)
elif respostaPrincipal == 2:
    print("-"*20, "[PROFESSORES]", "MENU DE OPERAÇÕES","-"*20)
elif respostaPrincipal == 3:
    print("-"*20, "[DISCIPLINAS]", "MENU DE OPERAÇÕES","-"*20)
elif respostaPrincipal == 4:
    print("-"*20, "[TURMAS]", "MENU DE OPERAÇÕES","-"*20)
elif respostaPrincipal == 5:
    print("-"*20, "[MATRICULAS]", "MENU DE OPERAÇÕES","-"*20)
elif respostaPrincipal == 6:
    print("-"*20,"[SAINDO]","-"*20)
    quit()
else:
    print("Opção Inválida!")
    quit()
    
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
    print("Voltar ao menu principal")

print("Finalizando aplicação...")