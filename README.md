  

# SISTEMA DE GERENCIAMENTO ACADEMICO - SISTEMA PUC

  

  

Esse projeto cria um sistema de gerenciamento academico, que gerencia estudantes, professores, turmas, matriculas e disciplinas, nelas posso incluir, atualizar e excluir informações.

  

  

## DESENVOLVIMENTO

1. Primeiro criamos uma lista vazia, `listaEstudantes`, em que armazenaremos os estudantes adicionados pelo usuário.

2.  `menuPrincipal()`: Essa função tem um loop while, pois queremos que o sistema continue rodando até que o usuário decida sair; Mostramos ao usuário onde ele se encontra: "Menu Principal" e em seguida mostramos as opções de gerenciamento que nosso sistema oferece, indicados com um número; Criamos uma variável chamada `opcao` que armazena a opção que o usuário escolheu(ação feita pela função `opcaoEscolhida()`); Criamos um dicionário com as chaves que são as opções que os usuários pode escolher e as suas respectivas funções de gerenciamento; Em seguida, verificamos se a opção que usuário escolheu é válida, ou seja, está entre os números 1 e 6, se o usuário digitar o número 6, signfica que ele quer sair, o sistema mostrará a mensagem "SAINDO" e dará um break no loop, para "quebrá-lo" e parar de rodar, Se o uusário digitar um número diferente destes, o sistema retornará uma mensagem escrita que a opção é inválida.

3.  `opcaoEscolhida()`: Essa função cria uma variável que armazena a opção escolhida pelo usuário, e tem como retorno a apenas a resposta.

4.  `enterParaContinuar()`: Essa função foi criada para facilitar quando precisamos pedir que o usuário pressione enter para continuar, então, ao invés de escrevermos o input toda vez, apenas chamamos a função que faz isso.

5.  `gerenciarEstudantes()`: Aqui nessa função, também temos um loop while, pois o menu de operações só deve parar de rodar quando o usuário decidir que quer voltar para o menu principal; Chamamos a função `menuOperacoes()` passando como argumento "ESTUDANTES", pois o usuário está dentro de Gerenciar Estudantes e armazenamos o retorno da função (a opção escolhida pelo usuário) dentro da variável `opcao`; Criamos um dicionário chamado `opcoes` contendo as opções que o usuário pode escolher(entre 1 a 5) e suas respectivas funções; Verificamos se a opção escolhida pelo usuário é válida, ou seja, está entre 1 a 5, se o usuário digitar 5 (voltar ao menu principal) paramos o loop com um break, o que faz o sistema voltar ao Menu Principal, e se o usuário digitar um número que não esteja dentro as opções, retornamos uma mensagem dizendo que essa opção é invalida e em seguida pedimos para o usuário pressionar ENTER para continuar usando nossa função `enterParaContinuar()` que criamos anteriormente.

6.  `gerenciarProfessores()`: Essa função retorna a mensagem "EM DESENVOLVIMENTO" pois essa parte do código ainda não foi desenvolvida.
7. `gerenciarDisciplinas()`,`gerenciarTurmas()`,`gerenciarMatriculas()`: Ainda está com o mesmo caso do `gerenciarProfessores()`, ainda não foi desenvolvido, e quando o usuário selecionar algumas dessas opções a mensagem "EM DESENVOLVIMENTO" aparecerá na tela.
8. `menuOperacos(escolhaMenuPrincipal)`: O argumento dessa função é utilizado para mostrar ao usuário com qual menu ele está interagindo; Printamos na tela o menu que ele está interagindo (ou seja, de estudantes, professores, matriculas, etc) e qual menu ele está: "MENU DE OPERAÇÕES"; Em seguida listamos as opções de ações que o usuário pode selecionar e usar; Essa função retorna a função `opcaoEscolhida`.
9. `incluirEstudante()`: Nessa função mostramos para o usuário onde ele está, ou seja, no sistema de "INCLUSÃO";
Armazenamos os dados do arquivo "estudantes.json" na variável `listaEstudantes` para que possamos manipular esses dados no programa;
Pedimos ao usuário para que informe o nome do estudante que ele deseja incluir e armazenamos a resposta na variável `nomeEstudante`; Pedimos ao usuário para que digite o código do estudante que está sendo adicionado e armazenamos a resposta na variável `codigoEstudante`; Por ultimo, pedimos para que o usuário digite o CPF do estudante e armazenamos a resposta dentro da variável `cpfEstudante`; Em seguida criamos um dicionário chamado `dicionarioEstudante`, dentro desse dicionario temos as chaves: "nome", "codigo" e "cpf", e seus respectivos valores são as variaveis `nomeEstudante`, `codigoEstudante`, `cpfEstudante`, ou seja, os valores dessas chaves são as respostas que o usuário digitou; Adicionamos, com a função `append()` o dicionário criado (`dicionarioEstudante`) dentro da lista vazia, que criamos lá no começo do código (`listaEstudantes`); 
Chamamos a função `salvarListaemJson` com os parametros "listaEstudantes" e "estudantes.json"), pois essa função escreve(write) o que foi passado dentro do arquivo em json; Chamamos a função `enterParaContinuar()` e por ultimo
10. `listarEstudantes()`: Essa função primeiro nos mostra onde estamos, ou seja, na "LISTAGEM"; 
Armazenamos, como na função acima, os dados do arquivo "estudantes.json" dentro da variavel listaEstudantes;
Com o if, verificamos se o length(comprimento da lista) é igual a 0 (ou seja, não tem nada nela) se for, mostramos uma mensagem dizendo que não há estudantes cadastrados; 
Rodamos um loop for para mostrarmos ao usuário cada estudante dentro da `listaEstudantes`; Por ultimo, chamamos a função `enterParaContinuar()`
11. `atualizarEstudantes()`: Essa função mostra o usuário onde ele está, ou seja, em "ATUALIZAÇÃO"; Perguntamos ao usuário qual código de estudante ele deseja editar e armazenamos o resultado na variável `estudanteASerEditado`; 
Armazenamos os dados do arquivo "estudantes.json" na variavel listaEstudante;
Em seguida criamos uma variável chamada `estudanteEditado`e colocamos o valor None nela(ou seja, a variável está vazia); Iniciamos um loop for, que percorre cada estudante na lista `listaEstudantes`, se encontrarmos um código igual ao que o usuário digitou, então armazenamos as informações do estudante encontrado na variável `estudanteEditado`, ao terminar, damos um break, pois já encontramos o código do estudante que o usuário estava procurando; Se o `estudanteEditado` continuar vazio, mostramos ao usuário que o código não foi encontrado, ou seja, o sistema não encontrou nenhum código igual ao que o usuário digitou na lista; Se não(ou seja, o código for encontrado) pedimos para que o usuário digite o novo código (o novo) e armazenamos o valor na variável `estudanteEditado` e substituimos o valor da chave ["codigo"] pelo qual o usuário digitou; Depois fazemos a mesma coisa ao pedir ao usuário o novo nome do estudante, substituindo o valor da chave ["nome"] pelo digitado e em seguida substituindo o valor da chave ["cpf"] pelo digitado; 
Mostramos ao usuário uma mensagem confirmando que o código escolhido foi atualizado;
Chamamos a função `salvarListaemJson(listaEstudantes, "estudantes.json)` para que seja escrito dentro do json as atualizações;
Por ultimo chamamos a função `enterParaContinuar()`
12. `excluirEstudante()`: Essa função primeiro, igual as outras, mostra ao usuário onde ele está: "EXCLUSÃO"; 
Armazenamos os dados do arquivo "estudantes.json" na variavel listaEstudante;
Em seguida perguntamos qual código o usuário deseja excluir e armazenamos a resposta na variável `codigoASerExcluido`, essa função funciona quase igual a anterior; Criamos uma variável chamada `estudanteRemovido` e atribuimos o valor None a ela, ou seja, a variável está vazia; Verificamos todos os estudantes de dentro da `listaEstudantes`; Se o código digitado pelo usuário for encontrado, colocamos as informações do estudante na variável `estudante`; Mostramos ao usuário a mensagem dizendo que o estudante com o código digitado foi removido e damos um break, pois ja achamos o código na lista; Se `estudanteRemovido` continuar None (ou seja, o sistema não encontrar o código igual ao que o usuário digitou na lista) vai aparecer uma mensagem dizendo que o código não foi encontrado; Se não, excluiomos o estudante da `listaEstudantes` usando a função `remove()`; 
Chamamos a função `salvarListaemJson(listaEstudantes, "estudantes.json)` para que seja escrito dentro do json as atualizações;
E por ultimo pedimos ao usuário pressionar enter para continuar, usando a função `enterParaContinuar()`.
13. `salvarListaemJson(lista, nome_arquivo)`: 
Essa função receve uma lista de dados e um nome de arquivo, escreve o conteúdo dessa lista em um arquivo JSON com o nome especificado;
O argumento "lista" é a lista de dados que queremos salvar em json e o "nome_arquivo" é o nome do arquivo onde queremos salvar esses dados; Abrimos o arquivo em modo escrita ("w") usando "with" para que nosso arquivo seja fechado corretamente após o uso; Abrimos o arquivo em modo escrita para que possamos escrever nele; Usamos a função `json.dump()`para escrever o conteudo da lista no arquivo json, essa função recebe três argumentos, a lista de dados que queremos escrever ("lista"), o arquivo onde queremos escrever esses dados ("arquivo") e "encure_ascii=False" para garantir que caracteres não ASCII sejam tratados corretamente; `json.dump()` converte a lista de daods em dados formato JSON e escreve esse JSON para o arquivo especificado;
14. `lerListaDoJson(nome_arquivo)`: Essa função lê os dados de um arquivo JSON, que será espeficiado quando chamada a função e retorna esses dados como uma lista; Usamos a estrutura de controle try/except, onde o try tenta executar um bloco de codigo e se alguma exceção ocorrer durante a execução desse bloco de codigo, o python irá lidar com o exceção de acordo com as instruções dentro do bloco "expect"; Aqui abrimos o arquivo JSON especificado no modo leitura ("r") para lermos os dados dele; Usamos a função `json.dump()` para ler os dados do arquivco json e armazená-los na variavel `dadosLidos`; A função `json.load()` converte o conteudo do arquivo json em um objeto python; Em `return dadosLidos` estamos retornando os dados lidos no arquivo json como uma lista. No except estamos dizendo que se ocorrer uma execeção durante a leitura do arquivo json, retornamos uma lista vazia "[]"