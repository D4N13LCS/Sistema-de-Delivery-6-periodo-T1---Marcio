Feature: Finalização de pedido

  Scenario: Finalizar pedido com sucesso
    Given um usuário com saldo e um produto
    When eu finalizar o pedido com pagamento pix
    Then o pedido deve ser criado com sucesso