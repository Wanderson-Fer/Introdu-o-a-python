from getpass import getuser
import datetime as dt
from os import system

# TESTE INTERNO
if __name__ == '__main__':  # O bloco de código principal
    print('Hello world')

    name = getuser()
    print(f'user: {name}')
    print(f'-- {dt.datetime.now()} --')
    system("PAUSE")
    print("DEPOIS DA PAUSA")

# Dicionário (dict) <- vários nomes, idades, alturas
# Manipulação de lista e dicionários (for)
