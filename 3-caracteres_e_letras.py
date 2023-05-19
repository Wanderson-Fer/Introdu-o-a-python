if __name__ == '__main__':
    print('Hello!')

    # 'strings' são trechos de texto delimitados entre aspas — simples ou
    # duplas — que podem ser atribuídas a variáveis e/ou manipuladas diretamente

    uma_string = "Isso é uma string"
    primeiro_nome = "John"
    sobrenome = "Locke"

    # Exibindo na tela o conteúdo da variável
    print(uma_string)
    # Concatenando ao exibir
    print('nome: ' + primeiro_nome)
    # Gerando uma variável a partir de uma concatenação
    nome_completo = primeiro_nome + ' ' + sobrenome
    print("O nome completo é " + nome_completo)

    # Interpolação — As 'strings' serão representadas por simpolos de '%s'
    print("O famoso filósofo %s ,mais conhecido por %s" % (nome_completo, sobrenome))

    # Símbolos usados na interpolação:
    # %s: string;
    # %d: inteiro;
    # %o: octal;
    # %x: hexacimal;
    # %f: real;
    # %e: real exponencial;
    # %%: sinal de percentagem.

    # 'strings' formatadas

    citacao = 'É preciso metade do tempo para usar a outra.'

    print(f'"{citacao}"\n frase de {nome_completo}')

    # 'slices' — Fatias de strings
    # nomeString[indiceInicial:indiceFinal]

    print(f'\nslices permitem mostrar uma string de forma '
          f'parcial capturando apenas uma fatia')
    print(f'\nparte da citação: {citacao[10:25]}')
