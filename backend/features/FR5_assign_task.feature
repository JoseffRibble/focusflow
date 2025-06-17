Feature: Assign Task to User
  As an authenticated user
  I want to assign a task to another user
  So that responsibilities can be delegated effectively

  Background:
    Given I am logged in
    And I have permission to assign tasks
    And a task titled "Prepare Q3 presentation" exists and is assignable
    And a user "alice" has an active account

  Scenario: Successfully assigning a task to another user
    When I select the task "Prepare Q3 presentation"
    And I assign the task to "alice"
    And I enter the assignment comment "Please complete by Friday"
    And I confirm the assignment
    Then I should see a confirmation message
    And the task should be assigned to "alice"
    And the assignment should be recorded in task history
    And "alice" should be notified

  Scenario: Attempting assignment without permission
    Given I do not have permission to assign tasks
    When I select the task "Prepare Q3 presentation"
    And I assign the task to "alice"
    And I confirm the assignment
    Then I should see an error message
    And the task should remain unassigned

  Scenario: Assignment fails due to system error
    Given the system encounters an update error
    When I select the task "Prepare Q3 presentation"
    And I assign the task to "alice"
    And I confirm the assignment
    Then I should see an error message
    And the task should remain unassigned
