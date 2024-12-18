from random import randint

class Carro:
    
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        self.distancia = 0
        
    def percorrer_distancia(self, distancia):
        self.distancia += distancia
        
def iniciar_jogo():
    
    ferrari = Carro('Ferrari', 'vermelha')
    porshe = Carro('Porshe', 'preto')
    
    while True:
        ferrari.percorrer_distancia(randint(0, 10))
        porshe.percorrer_distancia(randint(0, 10))
        
        if ferrari.distancia >= 100:
            print(f'O vencedor foi o carro {ferrari.marca} {ferrari.cor}')
            break
        
        if porshe.distancia >= 100:
            print(f'O vencedor foi o carro {porshe.marca} {porshe.cor}')
            break

iniciar_jogo()