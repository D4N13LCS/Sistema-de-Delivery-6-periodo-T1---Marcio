from orders.services.decorators import (
    Lanche,
    ExtraQueijo,
    Bacon,
    Catupiry
)


def test_lanche_com_adicionais():

    lanche = Lanche(
        "X-Tudo",
        35
    )

    lanche = ExtraQueijo(lanche)
    lanche = Bacon(lanche)
    lanche = Catupiry(lanche)

    assert lanche.preco() == 53