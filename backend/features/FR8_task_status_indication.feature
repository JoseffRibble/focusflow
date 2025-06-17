Feature: Visual Task Status Indicators
  As an authenticated user
  I want the system to visually indicate task statuses
  So that I can quickly understand the urgency and completion of tasks

  Background:
    Given I am logged in
    And I have access to the task list

  Scenario: Display visual indicators for various task statuses
    Given the current system time is "2025-06-10 10:00"
    And the following tasks exist
      | title             | due_date          | status      |
      | Submit report     | 2025-06-09 12:00   | In Progress |
      | Team sync-up      | 2025-06-10 15:00   | In Progress |
      | Code review       | 2025-06-15 09:00   | In Progress |
      | Finalize proposal | 2025-06-08 10:00   | Done        |
    When I view the task list
    Then I should see the following visual status indicators
      | title             | indicator |
      | Submit report     | Red       |
      | Team sync-up      | Yellow    |
      | Code review       | Yellow    |
      | Finalize proposal | Green     |

  Scenario: Task with invalid due date
    Given the current system time is "2025-06-10 10:00"
    And the following tasks exist
      | title        | due_date        | status      |
      | Broken task  | INVALID_DATE    | In Progress |
    When I view the task list
    Then I should see a warning icon next to "Broken task"
    And default styling should be applied to "Broken task"

  Scenario: Display update error
    Given the system encounters an update error
    When I view the task list
    Then the system should retain the previous indicators