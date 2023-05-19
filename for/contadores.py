if __name__ == '__main__':
    nomes = ['Wanderson', 'Gutemberg', 'Davi', 'Sabrina', 'Zilmara']

    contador = 0
    for nome in nomes:
        # contador = 0
        contador += 1

    if contador > 1:
        print('Há ' + str(contador) + ' nomes.')
    else:
        print('Há ' + str(contador) + ' nome.')
