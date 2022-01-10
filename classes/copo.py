# Desenvolva sua classe Copo aqui.
from .recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.bebida = None

    def encher(self, bebida: str="água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        self.sujar()
        self.conteudo = self.tamanho
        self.bebida = bebida

    def beber(self, quantidade: float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        self.conteudo = self.conteudo - quantidade
    def lavar(self):
        self.limpo = True
        self.conteudo = 0
        self.bebida = None
    def __repr__(self):
        return f"Um copo vazio de {float(self.tamanho)}ml" if self.conteudo <= 0 else f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"
