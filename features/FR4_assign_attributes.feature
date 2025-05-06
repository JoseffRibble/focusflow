Feature: Assign Task Organizational Attributes
  As an authenticated user
  I want to assign organizational attributes to tasks
  So that I can organize and filter tasks more effectively

  Background:
    Given I am logged in
    And I have permission to modify tasks
    And a task titled "Write quarterly summary" exists and is accessible

  Scenario: Successfully assigning valid organizational attributes
    When I select the task "Write quarterly summary"
    And I assign the project "Marketing"
    And I select the category "Reporting"
    And I set the area of responsibility to "Team A"
    And I click confirm to save attributes
    Then I should see a confirmation message
    And the task "Write quarterly summary" should have the project "Marketing"
    And the task should be categorized under "Reporting"
    And the task should be assigned to area "Team A"
    And the attribute changes should be recorded in task history

  Scenario: Attempting to assign invalid attribute combination
    When I select the task "Write quarterly summary"
    And I assign the project "Finance"
    And I select the category "Engineering"
    And I set the area of responsibility to "Team X"
    And I click confirm to save attributes
    Then I should see a validation error for invalid attribute combination
    And the task attributes should remain unchanged

  Scenario: Attribute update fails due to system error
    Given the system encounters an update error
    When I select the task "Write quarterly summary"
    And I assign the project "Operations"
    And I select the category "Logistics"
    And I set the area of responsibility to "Team Ops"
    And I click confirm to save attributes
    Then I should see an error message
    And the task attributes should remain unchanged
