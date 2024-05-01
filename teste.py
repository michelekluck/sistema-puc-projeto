def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        
def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        
processar_arquivo("exemplo.txt")
        