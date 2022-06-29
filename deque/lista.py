from collections import deque


class Lista:
    
    def __init__(self):
        self.lista = deque()

    def inserir(self, valor, pos=None):
        if pos:
            self.lista.insert(pos, valor)
        else:
            self.lista.append(valor)
    
    
    def remover(self, valor):
        return self.lista.remove(valor)
    
    
    def __repr__(self):
        return f'Lista [{", ".join(str(x) for x in self.lista)}]'


