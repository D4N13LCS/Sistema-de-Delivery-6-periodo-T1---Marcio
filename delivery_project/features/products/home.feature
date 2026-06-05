Feature: Home de produtos

  Scenario: Página paginada
    Given existem 15 produtos
    When acesso a home
    Then o status code deve ser 200
    And no máximo 6 produtos devem ser exibidos