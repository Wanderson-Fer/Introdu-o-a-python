# Definindo bloco de execução principal
if __name__ == '__main__':
    print("Hello world!")

    # 'Iteráveis' são objetos ou tipos em que podemos usar
    # um laço para tratar um ‘item’ por vez

    # Um 'iterável' pode é constituido por subpartes,
    # de maneira que pode ser dividido em fatias (slices),
    # e em itens individuais.

    # Strings
    string = 'Aqui jaz uma string'
    print("Uma string - " + string)

    # Fatia da string
    substring = string[13:]
    print("Uma substring - " + substring)

    # O número correspondente a um ‘item’ do objeto iterável
    # é conhecido por índice (index)

    # Um ‘item’ de uma ‘string’ é, na verdade, uma das suas letras

    # Primeira letra da cadeia de caracteres armazenada na variável "string"
    letra = string[0]
    print("Uma letra - " + letra)

    # NOTE que os índices começam em ZERO(0)

    # Iterando pela "string"
    print("Todas as letras da string")
    for item in string:
        print(item)
