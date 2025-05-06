Feature: Task Reminder Notifications
  As a system user
  I want to receive task reminders based on due dates
  So that I can stay informed and complete tasks on time

  Background:
    Given I am logged in
    And the system reminder service is operational

  Scenario: Send upcoming reminder 1 day before due date
    Given a task titled "Submit Q2 Report" is due on "2025-06-10 10:00"
    And "alice" is assigned to the task and has enabled reminders
    And the current system time is "2025-06-09 10:00"
    When the system checks for due reminders
    Then "alice" should receive a "upcoming" reminder
    And the reminder should include task title "Submit Q2 Report"

  Scenario: Send due today reminder
    Given a task titled "Team Meeting Agenda" is due on "2025-06-10 18:00"
    And "bob" is assigned to the task and has enabled reminders
    And the current system time is "2025-06-10 09:00"
    When the system checks for due reminders
    Then "bob" should receive a "due today" reminder
    And the reminder should include task title "Team Meeting Agenda"

  Scenario: Send overdue reminder
    Given a task titled "Fix security issue" is due on "2025-06-09 08:00"
    And "carol" is assigned to the task and has enabled reminders
    And the current system time is "2025-06-10 12:00"
    And the task is not completed
    When the system checks for due reminders
    Then "carol" should receive a "overdue" reminder
    And the reminder should include task title "Fix security issue"

  Scenario: No reminder sent for completed task
    Given a task titled "Update onboarding docs" is due on "2025-06-10 12:00"
    And the task is completed
    And "dan" is assigned to the task and has enabled reminders
    And the current system time is "2025-06-10 09:00"
    When the system checks for due reminders
    Then "dan" should not receive a reminder

  Scenario: Invalid due date skips reminder
    Given a task titled "Broken deadline task" has an invalid due date
    And "ellen" is assigned to the task and has enabled reminders
    And the current system time is "2025-06-10 10:00"
    When the system checks for due reminders
    Then the system should flag the task for due date review
