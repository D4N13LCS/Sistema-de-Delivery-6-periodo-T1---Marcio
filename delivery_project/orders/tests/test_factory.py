from orders.services.payment_factory import (
    PaymentFactory,
    PixPayment,
    CardPayment
)


def test_factory_pix():

    pagamento = (
        PaymentFactory.criar_pagamento(
            "pix"
        )
    )

    assert isinstance(
        pagamento,
        PixPayment
    )


def test_factory_cartao():

    pagamento = (
        PaymentFactory.criar_pagamento(
            "cartao"
        )
    )

    assert isinstance(
        pagamento,
        CardPayment
    )