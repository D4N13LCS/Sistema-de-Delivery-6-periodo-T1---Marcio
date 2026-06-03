from orders.services.delivery_strategy import (
    EntregaNormal,
    EntregaExpressa
)


def test_entrega_normal_gratis():

    strategy = EntregaNormal()

    assert strategy.calcular(60) == 0


def test_entrega_normal_padrao():

    strategy = EntregaNormal()

    assert strategy.calcular(30) == 5


def test_entrega_expressa():

    strategy = EntregaExpressa()

    assert strategy.calcular(100) == 20