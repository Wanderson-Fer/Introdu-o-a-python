if __name__ == '__main__':
    nomes = ['Wanderson', 'Gutemberg', 'Davi', 'Sabrina', 'Zilmara']

    sobrenomes = ['Fernandes', 'Borges', 'Primo', 'Tavares']

    nomes_completos = []

    # nomes_completos.append(nomes[0] + ' ' + sobrenomes[0])
    # nomes_completos.append(nomes[1] + ' ' + sobrenomes[1])
    # nomes_completos.append(nomes[2] + ' ' + sobrenomes[2])
    # nomes_completos.append(nomes[3] + ' ' + sobrenomes[3])

    # if len(nomes) != len(sobrenomes):
    #     print('Algo de errado não está certo')
    #     print('Abortando execução')
    #     exit()

    if len(nomes) > len(sobrenomes):
        sobrenomes.append('Alguma coisa')

    for indice in range(0, len(nomes)):
        novo_nome = nomes[indice] + ' ' + sobrenomes[indice]
        nomes_completos.append(novo_nome)

    # for nome in nomes_completos:
    #     print('>>>', nome)

    # print(nomes_completos)
