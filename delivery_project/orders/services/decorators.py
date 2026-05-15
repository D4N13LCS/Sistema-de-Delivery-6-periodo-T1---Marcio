class Lanche:

    def __init__(self, nome, preco):

        self.nome = nome

        self.valor = preco

    def descricao(self):
        return self.nome

    def preco(self):
        return self.valor


class ExtraQueijo:

    def __init__(self, lanche):

        self.lanche = lanche

    def descricao(self):
        return self.lanche.descricao() + " + Queijo"

    def preco(self):
        return self.lanche.preco() + 5


class Bacon:

    def __init__(self, lanche):

        self.lanche = lanche

    def descricao(self):
        return self.lanche.descricao() + " + Bacon"

    def preco(self):
        return self.lanche.preco() + 7


class Catupiry:

    def __init__(self, lanche):

        self.lanche = lanche

    def descricao(self):
        return self.lanche.descricao() + " + Catupiry"

    def preco(self):
        return self.lanche.preco() + 6