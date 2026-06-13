class WalletService:

    @staticmethod
    def debitar(perfil, valor):

        if perfil.saldo < valor:
            raise ValueError("Saldo insuficiente")

        perfil.saldo -= valor

        perfil.save()

class PixPayment:

    DESCONTO_PIX = 0.10

    def pagar(self, perfil, valor):

        desconto = valor * self.DESCONTO_PIX

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
        WalletService.debitar(perfil, valor)

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