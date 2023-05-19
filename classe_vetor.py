class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.vetor = []
        for x_axis in range(0, x):
            self.vetor.append([])
            for y_axis in range(0, y):
                self.vetor[x_axis].append([])
                for z_axis in range(0, z):
                    self.vetor[x_axis][y_axis].append(0)

    def __add__(self, other):
        if self.dimensoes == other.dimensoes
        pass

    def __repr__(self):
        return str(self.vetor)

    @property
    def dimensoes(self):
        return self.x, self.y, self.z

