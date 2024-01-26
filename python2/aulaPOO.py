class Carro:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0
        
    def abastercer(self, quantidade):
        self.qtd_de_combustivel += quantidade
        
if __name__ == '__main__':
    my_car = Carro()
    my_car.marca = "Fiat"
    my_car.modelo = "Uno"
    my_car.placa = "POP-1293"
    my_car.abastercer(10)
    my_car.abastercer(4)
    
    print(my_car.marca)
    print(my_car.qtd_de_combustivel)