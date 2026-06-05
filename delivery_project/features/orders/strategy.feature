Feature: Estratégia de entrega

  Scenario: Entrega normal grátis
    Given uma entrega normal
    When valor do pedido é 60
    Then frete deve ser 0

  Scenario: Entrega normal padrão
    Given uma entrega normal
    When valor do pedido é 30
    Then frete deve ser 5

  Scenario: Entrega expressa
    Given entrega expressa
    When valor do pedido é 100
    Then frete deve ser 20