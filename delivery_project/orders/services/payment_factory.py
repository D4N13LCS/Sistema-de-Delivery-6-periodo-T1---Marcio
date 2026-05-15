class PixPayment:

    def pagar(self, perfil, valor):

        desconto = valor * 0.10

        valor_final = valor - desconto

        if perfil.saldo < valor_final:

            raise Exception(
                "Saldo insuficiente"
            )

        perfil.saldo -= valor_final

        perfil.save()

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

    @staticmethod
    def criar_pagamento(tipo):

        if tipo == "pix":
            return PixPayment()

        return CardPayment()