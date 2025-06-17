Feature: Assign Task Due Date
  As an authenticated user
  I want to assign or modify due dates for tasks
  So that I can manage deadlines and prioritize work effectively

  Background:
    Given I am logged in
    And I have permission to modify tasks
    And a task titled "Design homepage" exists and is accessible

  Scenario: Successfully assigning a valid due date
    When I select the task "Design homepage"
    And I set the due date to "2025-06-01 17:00"
    Then I should see a confirmation message
    And the due date of task "Design homepage" should be "2025-06-01 17:00"
    And the due date change should be recorded in task history

  Scenario: Attempting to set a due date in the past
    When I select the task "Design homepage"
    And I set the due date to "2020-01-01 10:00"
    Then I should see a validation error for invalid date
    And the task due date should not be updated

  Scenario: Due date update fails due to system error
    Given the system encounters an update error
    When I select the task "Design homepage"
    And I set the due date to "2025-06-02 12:00"
    Then I should see an error message
    And the task due date should remain unchanged
