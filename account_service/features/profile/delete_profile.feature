Feature: Delete profile

  Scenario: Delete an existing profile
    Given an existing profile for user 1
    When I delete the profile
    Then the response status should be 200