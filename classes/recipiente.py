# Desenvolva sua classe Recipiente aqui.

class Recipiente:
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True):
        self.tamanho = tamanho if tamanho > 0 else 0
        self.conteudo = conteudo
        self.limpo = limpo
    def esvaziar(self):
        self.conteudo = 0
    def esta_vazio(self):
        return self.conteudo == 0 
    def lavar(self):
        self.conteudo = 0
        self.limpo = True   
    def esta_limpo(self):
        return self.limpo
    def estado(self):
        return "limpo" if self.limpo else "sujo"
    def sujar(self):
        self.limpo = False
    def __repr__(self):
        return f'Um recipiente {self.estado()} não especificado'