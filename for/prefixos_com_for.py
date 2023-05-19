if __name__ == '__main__':
    nomes = {
        'Wanderson': ['M', 'Solteiro'],
        'Gutemberg': ['M', 'Solteiro'],
        'Davi': ['M', 'Solteiro'],
        'Sabrina': ['F', 'Solteira'],
        'Zilmara': ['F', 'Solteira']
    }

    nomes_com_prefixo = []

    for nome in nomes:
        print('Chave ', nome)
        print('Valor ', nomes[nome])
        print('------------------------')
