# importando pacote para trabalhar com datas e chamando ele de 'dt'
import datetime as dt

# Definindo bloco de execução principal
if __name__ == '__main__':
    print("Hello world!")

    # E se, além de atender ao caso anterior,
    # pudessemos eliminar a nessecidade de
    # executar o programa várias vezes?

    # Inicializando o valor para comecar a executar o laço
    # Lendo um valor digitado por um amigo
    valor_digitado = int(input('Digite a sua idade ou o ano de nascimento: '))

    # Aqui será testado o valor digitado
    # Caso seja zero a execução do laço cessará
    while valor_digitado != 0:

        # Se o valor for maior que 100 é o ano de nascimento e não a idade
        if valor_digitado > 100:
            # Operação entre datas para obter a idade
            valor_digitado = int(dt.date.today().strftime('%Y')) - valor_digitado

        # O valor digitado agora corresponde à idade
        idade = valor_digitado

        # Verificando se é adulto
        if idade < 18:
            print('Não pode beber!')

        else:
            print('Pode beber!')

        # Lendo um valor digitado por um amigo
        # Para a próxima execução
        valor_digitado = int(input('Digite a sua idade ou o ano de nascimento:'
                                   '\n[OU digite ZERO (0) para sair]\n==> '))
