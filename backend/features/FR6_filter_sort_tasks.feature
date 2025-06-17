Feature: Filter and Sort Task List
  As an authenticated user
  I want to filter and sort my task list
  So that I can find relevant tasks efficiently

  Background:
    Given I am logged in
    And I have access to the task list
    And the following tasks exist:
      | title           | status     | due_date     | project     | category     | area      |
      | Buy groceries   | To Do      | 2025-06-01   | Personal    | Errands      | Home      |
      | Submit report   | Done       | 2025-05-15   | Work        | Reporting    | Team A    |
      | Fix bug #42     | In Progress| 2025-05-20   | Dev         | Bugs         | Team B    |

  Scenario: Successfully filtering tasks by status
    When I filter tasks by status "Done"
    Then I should see the following tasks:
      | title          |
      | Submit report  |

  Scenario: Successfully sorting tasks by due date ascending
    When I sort tasks by "due_date" in "ascending" order
    Then the task list should be ordered as:
      | title          |
      | Submit report  |
      | Fix bug #42    |
      | Buy groceries  |

  Scenario: Applying filter that yields no results
    When I filter tasks by status "Archived"
    Then I should see a "No tasks match criteria" message

  Scenario: Applying invalid filter combination
    When I apply a filter with status "Done" and area "Unknown Team"
    Then I should see a warning message about invalid filter combination
