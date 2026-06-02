from abc import ABC, abstractmethod


class ItemPedido(ABC):

    @abstractmethod
    def descricao(self):
        pass

    @abstractmethod
    def preco(self):
        pass

class Lanche(ItemPedido):

    def __init__(self, nome, preco):
        self.nome = nome
        self.valor = preco

    def descricao(self):
        return self.nome

    def preco(self):
        return self.valor
    
class AdicionalDecorator(ItemPedido):

    def __init__(self, item):
        self.item = item

class ExtraQueijo(AdicionalDecorator):

    PRECO = 5

    def descricao(self):
        return f"{self.item.descricao()} + Queijo"

    def preco(self):
        return self.item.preco() + self.PRECO


class Bacon(AdicionalDecorator):

    PRECO = 7

    def descricao(self):
        return f"{self.item.descricao()} + Bacon"

    def preco(self):
        return self.item.preco() + self.PRECO


class Catupiry(AdicionalDecorator):

    PRECO = 6

    def descricao(self):
        return f"{self.item.descricao()} + Catupiry"

    def preco(self):
        return self.item.preco() + self.PRECO