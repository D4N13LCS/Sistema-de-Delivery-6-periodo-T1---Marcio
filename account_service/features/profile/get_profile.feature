Feature: Get profile

  Scenario: Retrieve an existing profile
    Given an existing profile for user 1
    When I request the profile
    Then the response status should be 200
    And the returned user id should be 1