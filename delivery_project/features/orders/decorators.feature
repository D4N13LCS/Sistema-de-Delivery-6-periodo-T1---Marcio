Feature: Decorators de lanche

  Scenario: Lanche com adicionais
    Given um lanche X-Tudo custa 35
    When adiciono queijo, bacon e catupiry
    Then o preço final deve ser 53