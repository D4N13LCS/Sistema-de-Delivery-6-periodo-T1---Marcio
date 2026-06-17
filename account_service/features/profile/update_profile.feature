Feature: Update profile

  Scenario: Update address and card information
    Given an existing profile for user 1
    When I update the profile address to "New Address"
    Then the response status should be 200
    And the profile address should be "New Address"