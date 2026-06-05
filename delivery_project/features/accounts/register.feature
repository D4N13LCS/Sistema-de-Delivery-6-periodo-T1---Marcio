Feature: Registro de usuário

  Scenario: Acessar página de cadastro
    Given que acesso a página de registro
    When faço uma requisição GET
    Then o status code deve ser 200

  Scenario: Cadastro de usuário via interface
    Given que estou na página de registro
    When preencho username "usuario_teste"
    And preencho password "Senha@123"
    And clico no botão "Criar Conta"
    Then devo ser redirecionado para "/login/"