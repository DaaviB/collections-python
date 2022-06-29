from collections import deque


class Pilha:
    
    def __init__(self):
        self.pilha = deque()

    def inserir(self, valor):
            self.pilha.append(valor)
    
    def remover(self):
        return self.pilha.pop()
    
    
    def __repr__(self):
        return f'Pilha [{", ".join(str(x) for x in self.pilha)}]'

if __name__ == '__main__':
    p = Pilha()

    p.inserir(3)
    p.inserir(8)
    p.inserir(0)
    p.inserir(66)
    p.inserir(62)
    p.inserir(99)

    print(p)


    p.remover()
    p.remover()
    p.remover()

    print(p)
