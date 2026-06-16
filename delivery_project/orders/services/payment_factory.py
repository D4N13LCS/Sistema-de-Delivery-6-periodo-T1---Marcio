from accounts.gateways.account_gateway import AccountGateway

class WalletService:

    @staticmethod
    def debitar(usuario_id, valor):

        resultado = AccountGateway.debitar(
            usuario_id,
            valor,
        )

        if resultado is None:
            raise ValueError(
                "Serviço de contas indisponível."
            )

        return resultado

    @staticmethod
    def creditar(usuario_id, valor):

        resultado = AccountGateway.creditar(
            usuario_id,
            valor,
        )

        if resultado is None:
            raise ValueError(
                "Serviço de contas indisponível."
            )

        return resultado

class PixPayment:

    DESCONTO_PIX = 0.10

    def pagar(self, usuario_id, valor):

        desconto = valor * self.DESCONTO_PIX
        valor_final = valor - desconto

        WalletService.debitar(
            usuario_id,
            valor_final,
        )

        return {
            "valor_final": valor_final,
            "desconto": desconto,
            "mensagem": "PIX aprovado"
        }


class CardPayment:

    def pagar(self, usuario_id, valor):

        WalletService.debitar(
            usuario_id,
            valor,
        )

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