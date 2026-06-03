from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):

    @abstractmethod
    def calcular(self, subtotal):
        pass


class EntregaNormal(DeliveryStrategy):

    def calcular(self, subtotal):

        taxa_base = 5

        if subtotal > 50:
            return 0

        return taxa_base


class EntregaExpressa(DeliveryStrategy):

    def calcular(self, subtotal):

        taxa_base = 15

        taxa_prioridade = subtotal * 0.05

        return taxa_base + taxa_prioridade

