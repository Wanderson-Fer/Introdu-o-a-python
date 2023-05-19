if __name__ == '__main__':
    # Adicione o prefixo 'SR.' para os seguntes nomes

    nomes = ['Wanderson', 'Gutemberg', 'Davi', 'Sabrina', 'Zilmara']

    nomes_com_prefixo = []

    # nomes_com_prefixo = 'Sr. ' + nomes[0]
    #
    # print(nomes_com_prefixo)

    for prefixo in range(0, len(nomes)):
        novo_nome = 'Sr. ' + nomes[prefixo]
        # print(novo_nome)
        nomes_com_prefixo.append(novo_nome)

    for nome in nomes_com_prefixo:
        print('- ', nome)
