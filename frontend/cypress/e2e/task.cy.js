describe("Task Dashboard", () => {
  let testUser;
  let taskTitle;

  // Register test user once before all tests
  before(() => {
    cy.registerUser().then((user) => {
      testUser = user;
    });
  });

  // Login before each test and prepare a unique task title
  beforeEach(() => {
    cy.clearCookies();
    cy.clearLocalStorage();
    taskTitle = `UI Test Task ${Date.now()}`;

    cy.loginUser(testUser).then(() => {
      cy.visit("http://localhost:5173/tasks");
    });
  });

  it("creates a new task", () => {
    cy.get('input[placeholder="Title"]').type(taskTitle);
    cy.get('input[placeholder="Short Description"]').type("Short");
    cy.get('input[placeholder="Long Description"]').type("Long");
    cy.get('input[type="date"]').type("2025-12-31");
    cy.get('[data-cy="create-priority"]').select("HIGH");
    cy.contains("Create Task").click();

    cy.contains(taskTitle, { timeout: 10000 }).should("exist");
  });

  it("changes task status", () => {
    // Create task via API
    cy.createTask({
      title: taskTitle,
      short_description: "Short",
      long_description: "Long",
      due_date: "2025-12-31",
      priority: "HIGH",
    });

    cy.reload(); // Refresh to load latest tasks

    cy.contains(taskTitle, { timeout: 10000 }).should("exist");

    // Change status to CLOSED and verify
    cy.contains(taskTitle)
      .parents("[data-cy^='task-']")
      .within(() => {
        cy.get("select").select("CLOSED");
        cy.get("select", { timeout: 10000 }).should("have.value", "CLOSED");
      });
  });

  it("deletes a task", () => {
    // Create task via API
    cy.createTask({
      title: taskTitle,
      short_description: "Short",
      long_description: "Long",
      due_date: "2025-12-31",
      priority: "HIGH",
    });

    cy.reload(); // Refresh to load latest tasks

    cy.contains(taskTitle, { timeout: 10000 }).should("exist");

    // Delete the task
    cy.contains(taskTitle)
      .parents("[data-cy^='task-']")
      .within(() => {
        cy.contains("Delete").click();
      });

    // Verify task is removed from UI
    cy.contains(taskTitle, { timeout: 10000 }).should("not.exist");

    // Confirm task is gone via API
    cy.getAuthToken().then((token) => {
      cy.request({
        method: "GET",
        url: "http://127.0.0.1:8000/api/tasks/",
        headers: { Authorization: `Bearer ${token}` },
      }).then((response) => {
        const exists = response.body.some((t) => t.title === taskTitle);
        expect(exists).to.be.false;
      });
    });
  });
});
