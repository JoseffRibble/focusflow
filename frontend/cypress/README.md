# UI Testing with Cypress

## Prerequisites

- Node.js and npm installed
- Backend API server running at `http://localhost:8000`
- Frontend development server running at `http://localhost:5173`
- A test user will be created dynamically by Cypress (no need to pre-create)



## Running Cypress Tests

### 1. Install dependencies

```bash
cd frontend
npm install
```

### 2. Open Cypress UI (interactive)

```bash
npx cypress open
```

### 3. Run Cypress headlessly (CI-friendly)

```bash
npx cypress run
```


## Test Coverage

### `login.cy.js`

- Successful login with correct credentials
- Login failure with incorrect password

### `task.cy.js`

- Create a task with a unique title
- Update task status via dropdown
- Delete a task and assert it's removed from both UI and API



## Custom Cypress Commands

Located in `cypress/support/commands.js`:

```js
// Registers a user with a unique username/email
Cypress.Commands.add("registerUser", () => { ... });

// Logs in the given user and stores token
Cypress.Commands.add("loginUser", (user) => { ... });

// Gets the token from localStorage
Cypress.Commands.add("getAuthToken", () => { ... });

// Creates a task via API
Cypress.Commands.add("createTask", (task) => { ... });
```



## Test Isolation

Each test:
- Registers a fresh user (once per suite)
- Logs in and clears localStorage before running
- Creates a unique task per test to avoid interference
