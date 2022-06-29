from collections import deque


class Fila:
    
    def __init__(self):
        self.fila = deque()

    def inserir(self, valor):
            self.fila.append(valor)
    
    def remover(self):
        return self.fila.popleft()
    
    
    def __repr__(self):
        return f'Fila [{", ".join(str(x) for x in self.fila)}]'

if __name__ == '__main__':
    
    f = Fila()

    f.inserir(3)
    f.inserir(8)
    f.inserir(0)
    f.inserir(66)
    f.inserir(62)
    f.inserir(99)

    print(f)


    f.remover()
    f.remover()
    f.remover()

    print(f)
