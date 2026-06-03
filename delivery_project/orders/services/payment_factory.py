class WalletService:

    @staticmethod
    def debitar(perfil, valor):

        if perfil.saldo < valor:
            raise Exception(
                "Saldo insuficiente"
            )

        perfil.saldo -= valor

        perfil.save()

class PixPayment:

    def pagar(self, perfil, valor):

        desconto = valor * 0.10

        valor_final = valor - desconto

        WalletService.debitar(
            perfil,
            valor_final
        )

        return {
            "valor_final": valor_final,
            "desconto": desconto,
            "mensagem": "PIX aprovado"
        }


class CardPayment:

    def pagar(self, perfil, valor):

        if perfil.saldo < valor:

            raise Exception(
                "Saldo insuficiente"
            )

        perfil.saldo -= valor

        perfil.save()

        return {
            "valor_final": valor,
            "desconto": 0,
            "mensagem": "Cartão aprovado"
        }


class PaymentFactory:

    PAYMENTS = {
        "pix": PixPayment,
        "cartao": CardPayment
    }

    @classmethod
    def criar_pagamento(cls, tipo):

        pagamento = cls.PAYMENTS.get(tipo)

        if not pagamento:
            raise ValueError(
                "Forma de pagamento inválida"
            )

        return pagamento()