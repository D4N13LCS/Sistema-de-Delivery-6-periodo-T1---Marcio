Feature: Listagem vazia

  Scenario: Não existem produtos cadastrados
    Given não existem produtos cadastrados
    When acesso a API de produtos
    Then devo receber uma lista vazia