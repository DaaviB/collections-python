from collections import namedtuple
from pprint import pprint

if __name__ == '__main__':
    Jogador = namedtuple('Jogador', ['nome', 'camisa', 'time'])
    jogador_1 = Jogador('Carlos', 10, 'Ceará')
    print(jogador_1)
    print(jogador_1.nome)
    print(jogador_1.time)
    print(jogador_1.camisa)

# =====================================
    carta = namedtuple('Carta', 'naipe valor')
    naipes = 'p C O E'.split()
    valores = list(range(2, 11)) + 'A J Q K'.split()
    
    baralho = [carta(naipe, valor) for naipe in naipes for valor in valores]

    
    print(naipes)
    print(valores)
    pprint(baralho)
