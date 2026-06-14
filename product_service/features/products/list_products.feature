Feature: Listagem de produtos

  Scenario: Consultar produtos cadastrados
    Given existem produtos cadastrados
    When acesso a API de produtos
    Then devo receber uma lista de produtos