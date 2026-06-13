from abc import ABC, abstractmethod


class ItemPedido(ABC):

    @abstractmethod
    def descricao(self):
        raise NotImplementedError

    @abstractmethod
    def preco(self):
        raise NotImplementedError

class Lanche(ItemPedido):

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco_base = preco

    def descricao(self):
        return self.nome

    def preco(self):
        return self.preco_base
    
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