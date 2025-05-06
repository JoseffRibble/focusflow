Feature: View Tasks in Timeline or Calendar
  As an authenticated user
  I want to view my tasks organized by due dates in a timeline or calendar
  So that I can manage schedules and deadlines visually

  Background:
    Given I am logged in
    And I have access to the task list

  Scenario: Display tasks in calendar view with valid due dates
    Given the following tasks exist with due dates
      | title           | due_date   |
      | Final report    | 2025-06-10 |
      | Team meeting    | 2025-06-12 |
      | Code review     | 2025-06-14 |
    When I switch to the calendar view
    Then I should see tasks arranged by their due dates
      | title         | date       |
      | Final report  | 2025-06-10 |
      | Team meeting  | 2025-06-12 |
      | Code review   | 2025-06-14 |

  Scenario: Display tasks in timeline view with time range navigation
    Given the following tasks exist with due dates
      | title           | due_date   |
      | Final report    | 2025-06-10 |
      | Presentation    | 2025-06-15 |
    When I switch to the timeline view
    And I navigate to the week of "2025-06-09"
    Then I should see the following tasks in timeline
      | title         |
      | Final report  |
      | Presentation  |

  Scenario: No tasks with due dates
    Given no tasks with due dates exist
    When I switch to the calendar view
    Then I should see a "No scheduled tasks" message

  Scenario: View fails to load due to system error
    Given the system encounters an update error
    When I switch to the timeline view
    Then I should see an error message
