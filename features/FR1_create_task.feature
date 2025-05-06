Feature: Create New Task
  As an authenticated user
  I want to create a new task by providing title, description, and context
  So that I can manage my work effectively in the system

  Background:
    Given I am logged in
    And I have permission to create tasks

  Scenario: Successfully creating a new task with title only
    When I click the "Create New Task" button
    And I enter "Buy groceries" as the task title
    And I click the "Save" button
    Then I should see a success message
    And the task "Buy groceries" should appear in my task list

  Scenario: Successfully creating a new task with all optional fields
    When I click the "Create New Task" button
    And I enter "Write project report" as the task title
    And I add a description "Summarize Q2 results"
    And I associate the task with the project "Q2 Analytics"
    And I assign the category "Documentation"
    And I add tags "report", "quarterly"
    And I upload the file "summary.docx"
    And I click the "Save" button
    Then I should see a success message
    And the task "Write project report" should appear in my task list

  Scenario: Creating a task with invalid input (missing title)
    When I click the "Create New Task" button
    And I leave the title field empty
    And I click the "Save" button
    Then I should see a validation error for the title field
    And the task should not be created

  Scenario: Task creation fails due to a system storage error
    Given the system encounters a storage error
    When I create a task titled "Buy snacks"
    Then I should see an error message
    And the task should not appear in my task list
