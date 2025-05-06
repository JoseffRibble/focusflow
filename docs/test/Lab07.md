# Exercise 7 – BDD & Gherkin Syntax

- All documentation was reviewed using ChatGPT to ensure grammatical accuracy.
- All use cases were reviewed using ChatGPT to ensure complete feature coverage.
- The project uses the behave package for BDD testing.
- All dependencies, including behave, are defined in environment.yml and are automatically installed when setting up the environment.

## 7.1 & 7.2 – Running BDD Tests

To run the BDD tests, execute the following command from the root directory of the project:
```
behave
```
This will automatically detect and execute all scenarios defined in the feature files located in the features/ directory.

## 7.3 – BDD Test Automation
BDD tests are best executed during the **integration test stage**. This is because they validate the system's behavior from the user's perspective, involving multiple components working together. Executing them at this stage ensures that higher-level business requirements are being met across integrated parts of the system.