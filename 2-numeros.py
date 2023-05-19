if __name__ == '__main__':
    print('Hello')
    print('Variáveis e seus tipos')
    print('===============================')

    # Números -

    # Inteiros -
    numero1 = 2
    numero2 = 5

    print('O primeiro número é ', numero1,
          '\nO segundo número é ' + str(numero2))
    # Obs.: o primeiro número foi exibido como mais um argumento
    # da função 'print()', já o segundo, foi concatenado, após a sua
    # conversão para 'string', com a função 'str()'

    print('-----------------------------------')

    print('Verificando o tipo:')
    print('Número 1 - ' + str(type(numero1)),
          '\nNúmero 2 - ' + str(type(numero2)))

    # Operações entre inteiros
    print('-----------------------------------')

    resultado_soma = numero1 + numero2
    print('Soma: ' + str(resultado_soma),
          'e seu tipo: ' + str(type(resultado_soma)))

    resultado_subtracao = numero1 - numero2
    print('Subtração: ' + str(resultado_subtracao),
          'e seu tipo: ' + str(type(resultado_subtracao)))

    resultado_multiplicacao = numero1 * numero2
    print('Multiplicação: ' + str(resultado_multiplicacao),
          'e seu tipo: ' + str(type(resultado_multiplicacao)))

    # Números com ponto flutuante ou reais

    resultado_divisao = numero1 / numero2
    print('Divisão: ' + str(resultado_divisao),
          'e seu tipo: ' + str(type(resultado_divisao)))
    # Operações de divisão resultam, automaticamente, em 'float'

    print('-----------------------------------')
    # Conversões - (também conhecidar por operações de coerção)

    print("Convertendo um float em int: ")
    print('Em float - ', 3.75,
          ' >> Em inteiro - ', round(3.75))
    # Note haver uma perda de informação para essa conversão,
    # por esse motivo ela não é recomendada

    print('-----------------------------------')
    # A função 'round()' também pode ser usada para
    # delimitar quantidade de casas decimais

    print('Limitando quantidade de casas após a vírgula:')
    print('Float - ', 3.757423,
          ' >> limitando á duas casas - ', round(3.753423, 2))

    # Operações boleanas
    # Resultam em 'True' ou 'False'
    print('-----------------------------------')
    print('Operações booleanas')

    print("'numero1' é maior que 'numero2'?",
          numero1 > numero2)
    print("'numero1' é menor que 'numero2'?",
          numero1 < numero2)
    print("'numero1' é igual a 'numero2'?",
          numero1 == numero2)
    print("'numero1' é diferente de 'numero2'?",
          numero1 != numero2)
