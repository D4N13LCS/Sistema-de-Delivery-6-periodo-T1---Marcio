Feature: Debit balance

  Scenario: Debit with sufficient balance
    Given a profile with balance 100
    When I debit 40
    Then the balance should become 60

  Scenario: Debit with insufficient balance
    Given a profile with balance 20
    When I debit 50
    Then the response status should be 400