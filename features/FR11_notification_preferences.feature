Feature: Configure Notification Preferences
  As a system user
  I want to customize my notification settings
  So that I can stay informed without being overwhelmed

  Background:
    Given I am logged in
    And the notification system is operational

  Scenario: Successfully updating notification preferences
    Given my current notification settings are:
      | type      | enabled | channel   |
      | task      | true    | email     |
      | reminder  | false   | in-app    |
    When I update my notification preferences to:
      | type      | enabled | channel   |
      | task      | false   | in-app    |
      | reminder  | true    | email     |
    Then my updated preferences should be:
      | type      | enabled | channel   |
      | task      | false   | in-app    |
      | reminder  | true    | email     |
    And I should see a confirmation of saved changes

  Scenario: Invalid configuration combination
    Given my current notification settings are:
      | type    | enabled | channel |
      | alert   | true    | none    |
    When I update my notification preferences to:
      | type    | enabled | channel |
      | alert   | true    | none    |
    Then I should see an error about invalid channel selection
    And my preferences should remain unchanged

  Scenario: Save failure during update
    Given my current notification settings are:
      | type    | enabled | channel |
      | task    | true    | email   |
    And the system encounters a save error
    When I update my notification preferences to:
      | type    | enabled | channel |
      | task    | false   | in-app  |
    Then I should see an error message
    And my preferences should remain unchanged
