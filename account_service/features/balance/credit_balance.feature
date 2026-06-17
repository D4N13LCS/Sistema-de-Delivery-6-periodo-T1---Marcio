Feature: Credit balance

  Scenario: Credit user balance
    Given a profile with balance 100
    When I credit 50
    Then the balance should become 150