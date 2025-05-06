Feature: Update Task Status
  As an authenticated user
  I want to update the status of tasks to reflect their progress
  So that I can track work effectively and visualize task progression

  Background:
    Given I am logged in
    And I have permission to modify tasks
    And a task titled "Submit report" exists and is accessible

  Scenario: Successfully updating task status to In Progress
    When I select the task "Submit report"
    And I change the status to "In Progress"
    Then I should see a confirmation message
    And the status of task "Submit report" should be "In Progress"
    And the status change should be recorded in task history

  Scenario: Successfully updating task status to Done with a comment
    When I select the task "Submit report"
    And I change the status to "Done"
    And I enter the comment "Work completed"
    Then I should see a confirmation message
    And the status of task "Submit report" should be "Done"
    And the comment "Work completed" should be saved with the status change

  Scenario: Attempting invalid status transition
    When I select the task "Submit report"
    And I attempt to change the status to "Archived"
    Then I should see an error message about invalid status
    And the status of task "Submit report" should remain unchanged

  Scenario: Task status update fails due to system error
    Given the system encounters an update error
    When I select the task "Submit report"
    And I change the status to "In Progress"
    Then I should see an error message
    And the status of task "Submit report" should remain unchanged
