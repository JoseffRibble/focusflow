Feature: Send Task Assignment Notifications
  As a user of the system
  I want to be notified of task assignments and updates
  So that I can stay informed about my responsibilities

  Background:
    Given a user "alice" exists and has enabled notifications
    And the notification service is operational

  Scenario: Notify user on new task assignment
    When a task titled "Prepare Q4 Report" is assigned to "alice"
    Then "alice" should receive a notification about the assignment
    And the notification should include the task title and description
    And the notification should be logged

  Scenario: Notify user on task status update
    Given a task titled "Submit budget proposal" is assigned to "alice"
    When the status of task "Submit budget proposal" changes to "In Progress"
    Then "alice" should receive a notification about the status update
    And the notification should include the new status
    And the notification should be logged

  Scenario: Notify user on due date change
    Given a task titled "Finalize slides" is assigned to "alice"
    When the due date of task "Finalize slides" changes to "2025-06-15"
    Then "alice" should receive a notification about the due date change
    And the notification should include the new due date
    And the notification should be logged

  Scenario: Notification delivery failure
    Given a task titled "Write report" is assigned to "alice"
    And "alice" has an invalid email address
    When a notification is triggered
    Then the system should attempt to retry delivery 3 times
    And the system should mark the notification as failed
    And "alice" should see the notification in the in-app center
