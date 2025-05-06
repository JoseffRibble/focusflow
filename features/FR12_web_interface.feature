Feature: Access Web-Based User Interface
  As a system user
  I want to access the task management interface from any device
  So that I can manage my tasks with a responsive and consistent experience

  Background:
    Given the system is operational

  Scenario Outline: Load appropriate interface version based on device
    Given I have a compatible "<device>" with "<browser>" and screen width of <width>
    When I access the system URL
    Then I should see the "<layout>" layout loaded
    And my theme preference should be applied

    Examples:
      | device   | browser      | width | layout  |
      | Desktop  | Chrome       | 1280  | Desktop |
      | Tablet   | Safari       | 768   | Tablet  |
      | Mobile   | Firefox      | 375   | Mobile  |

  Scenario: Incompatible browser detected
    Given I have an incompatible "Internet Explorer" browser
    When I access the system URL
    Then I should see a browser compatibility warning

  Scenario: Access with poor connection
    Given I have a stable browser "Chrome"
    And my connection speed is "slow"
    When I access the system URL
    Then the system should enable offline mode
    And I should see a connection status indicator

  Scenario: Successful login and personalized dashboard
    Given the system is operational
    And I have a compatible "desktop" with "Chrome" and screen width of 1280
    And my connection speed is "fast"
    And I have valid credentials
    When I access the system URL
    And I log in successfully
    Then I should see the "Desktop" layout loaded
    And my personalized dashboard should load

