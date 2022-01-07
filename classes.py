class Automovel:

    def __init__(self, marca, modelo, cor, motor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.motor = motor
        self.veiculos = []

    def constroi_veiculo(self):
        self.veiculos.append(Veiculo(self.marca, self.modelo, self.cor, self.motor))

    def exibe_carro(self):
        for veiculo in self.veiculos:
            print(veiculo.marca , veiculo.modelo, veiculo.cor, veiculo.motor)


    def andar(self):
        print('O carro está andando')

    def parar(self):
        if not self.andar():
            print('O carro não esta andando')

        print('O carro esta parando')


class Veiculo(Automovel):
   pass










