// Register a new user with a unique email and username
Cypress.Commands.add("registerUser", () => {
  const uniqueSuffix = Date.now();
  const user = {
    username: `testuser_${uniqueSuffix}`,
    email: `testuser_${uniqueSuffix}@example.com`,
    password: "testpass123",
  };

  return cy
    .request({
      method: "POST",
      url: "http://127.0.0.1:8000/api/register/",
      body: user,
      headers: {
        "Content-Type": "application/json",
      },
      failOnStatusCode: false,
    })
    .then((response) => {
      // Allow 409 if user already exists
      if (response.status === 409) {
        return user;
      }

      expect([200, 201]).to.include(response.status);
      return user;
    });
});

// Log in with given user and store token in localStorage
Cypress.Commands.add("loginUser", (user) => {
  return cy
    .request({
      method: "POST",
      url: "http://127.0.0.1:8000/api/login/",
      body: {
        email: user.email,
        password: user.password,
      },
    })
    .then((response) => {
      const token = response.body.access;
      return cy.window().then((win) => {
        win.localStorage.setItem("token", token);
      });
    });
});

// Retrieve auth token from localStorage
Cypress.Commands.add("getAuthToken", () => {
  return cy.window().then((win) => win.localStorage.getItem("token"));
});

// Create a task using API and auth token
Cypress.Commands.add("createTask", (task) => {
  cy.getAuthToken().then((token) => {
    cy.request({
      method: "POST",
      url: "http://127.0.0.1:8000/api/tasks/",
      headers: { Authorization: `Bearer ${token}` },
      body: task,
    });
  });
});
