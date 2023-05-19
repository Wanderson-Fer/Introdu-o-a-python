class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0.0

    def mover(self, km):
        print(f'{km} km foram percorridos')
        self.tanque -= km * self.consumo

    def gasolina(self):
        return self.tanque

    def abastecer(self, litros):
        print(f'{litros} litros de combustível foram adicionados ao tanque')
        self.tanque += litros


if __name__ == '__main__':
    gol = Carro(0.5)
    gol.abastecer(5)
    print(f'{gol.gasolina()}L no tanque')
    gol.mover(5)
    print(f'{gol.gasolina()}L no tanque')
