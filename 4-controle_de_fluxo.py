# importando pacote para trabalhar com datas e chamando ele de 'dt'
import datetime as dt

# Definindo bloco de execução principal
if __name__ == '__main__':
    print("Hello world!")

    # Temos a seguinte questão:
    # Ao realizar uma festa, com bebida grátis,
    # em que alguns dos seus amigos são menores de idade.
    # Como verificar quem pode e quem não pode beber, apenas com a idade?
    # E, se fosse, pudessem digitar a data de nascimento?

    # Lendo um valor digitado por um amigo
    valor_digitado = int(input('Digite a sua idade ou o ano de nascimento:'))

    # Se o valor for maior que 100 é o ano de nascimento e não a idade
    if valor_digitado > 100:
        # Operação entre datas para obter a idade
        ano_atual = int(dt.date.today().strftime('%Y'))
        valor_digitado = ano_atual - valor_digitado

        print('Você digitou um ano de nascimento')
        print('Sua idade é %d' % (valor_digitado))

    # O valor digitado agora corresponde à idade
    idade = valor_digitado

    # Verificando se é adulto
    if idade < 18:
        print('Não pode beber!')
    elif idade > 100:
        print('Você é uma múmia?')
    else:
        print('Pode beber!')
