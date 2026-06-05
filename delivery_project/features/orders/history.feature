Feature: Histórico de pedidos

  Scenario: Usuário logado acessa histórico
    Given um usuário autenticado
    When acesso "/historico/"
    Then o status code deve ser 200