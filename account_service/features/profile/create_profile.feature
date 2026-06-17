Feature: Create profile

  Scenario: Successfully create a profile
    Given a user id 1
    When a profile is created with balance 200 and address "Main Street"
    Then the response status should be 201
    And the profile balance should be 200