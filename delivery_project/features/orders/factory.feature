Feature: Factory de pagamento

  Scenario: Criar pagamento pix
    When eu criar pagamento "pix"
    Then o tipo deve ser PixPayment

  Scenario: Criar pagamento cartão
    When eu criar pagamento "cartao"
    Then o tipo deve ser CardPayment