if __name__ == "__main__":
    print('Hello')
    print('Algumas variaveis:')

    # Isso é um comentário
    # Alguns exemplos de declaração de variáveis abaixo

    # Palavras e frases sempre estarão entre aspas simples ou duplas
    name = 'Wanderson'  # string (str)
    idade = 20  # integer (int)
    peso = 70.2  # float (float)
    dirige = False  # boolean (bool)
    bebe = True  # boolean (bool)

    print('Nome:', name)  # 'Wanderson'
    print('Idade:', idade)  # 20
    print('Peso:', peso)  # 70.2
    print('Dirige?', dirige)  # False
    print('Bebe?', bebe)  # True

    print('Tipo dos dados: ')

    print(type(name))  # <class 'str'>
    # 'str' é a abreviação para 'string', sendo a palavra-chave para dados do tipo 'texto'
    print(type(idade))  # <class 'int'>
    # 'int' é palavra-chave para 'números inteiros', abreviação de 'integer'
    print(type(peso))  # <class 'float'>
    # 'float' é a palavra-chave para 'números com casas decimais',
    # chamados também de 'números com pontos flutuantes', vulgo reais
    print(type(dirige))  # <class 'bool'>
    # 'bool' é a abreviação para 'boleanos',
    # valores binários que alternam entre 'verdadeiro' e 'falso'.
    # Boleanos são úteis para trabalhar com estruturas de decisão, como o 'if', por exemplo
    print(type(bebe))  # <class 'bool'>

    print('Done')
