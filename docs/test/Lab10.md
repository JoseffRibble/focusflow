# Exercise 10 – UI / E2E Testing 

## 10.1 - Implement UI for FocusFlow

We have implemented the UI for the following pages:
- Login Page
- Task Dashboard with Kanban-style columns
- Task creation, editing, status update, and deletion

The UI is built using **React**, and communicates with a Django backend via REST API.

![Login Screenshot](/docs/images/UI/login_page.png)
![Task Dashboard Screenshot](/docs//images/UI/task_dashboard.png)

## 10.2 - Automate UI or E2E Tests

Automated E2E tests are written using **Cypress** and located in `frontend/cypress/e2e/`.

Test coverage includes:
- User login (success and failure)
- Creating a task
- Updating task status
- Deleting a task

**Details**: [UI Testing with Cypress](/frontend/cypress/README.md)

## 10.3 - Execute & Document your tests

Tests were executed in both:
- Headless mode via `npx cypress run`
- Interactive GUI via `npx cypress open`

### Results
#### Headless mode

![10_headless_mode-1](/docs/images/test_result/10_headless_mode-1.png)
![10_headless_mode-2](/docs/images/test_result/10_headless_mode-2.png)

#### Interactive GUI

![10_interactive_GUI-1](/docs/images/test_result/10_interactive_GUI-1.png)
![10_interactive_GUI-2](/docs/images/test_result/10_interactive_GUI-2.png)

### Reeflection
#### What was easy
- Writing custom commands and using API requests made it easy to set up consistent state before each test.
- Cypress’s `.within()` and `.contains()` chaining made it easy to scope actions inside a task card.

#### What was difficult
- Ensuring the UI had fully re-rendered before assertions was challenging at first.
- Debugging failed tests due to shared task titles led to several false negatives before resolved.