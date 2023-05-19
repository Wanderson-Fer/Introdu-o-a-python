class quadrado:

    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, lado):
        self.lado = lado

    @property
    def calcular_area(self):
        return self.lado**2


if __name__ == '__main__':
    square = quadrado(2)
    print(square.get_lado())
    print(square.calcular_area)
    print(square.set_lado(3))
    print(square.get_lado())
    print(square.calcular_area)
