Feature: Fluxo de pedido

  Scenario: Acessar tela de pedido autenticado
      Given um usuário autenticado
      When acesso "/pedido/"
      Then o status code deve ser 200