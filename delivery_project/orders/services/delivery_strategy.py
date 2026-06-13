from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):

    @abstractmethod
    def calcular(self, subtotal):
        raise NotImplementedError


class EntregaNormal(DeliveryStrategy):

    TAXA_NORMAL = 5
    LIMITE_FRETE_GRATIS = 50

    def calcular(self, subtotal):

        if subtotal > self.LIMITE_FRETE_GRATIS:
            return 0

        return self.TAXA_NORMAL


class EntregaExpressa(DeliveryStrategy):

    TAXA_EXPRESSA = 15
    PERCENTUAL_PRIORIDADE = 0.05

    def calcular(self, subtotal):
        taxa_prioridade = subtotal * self.PERCENTUAL_PRIORIDADE

        return self.TAXA_EXPRESSA + taxa_prioridade

