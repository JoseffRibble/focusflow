describe("Login Page", () => {
  let testUser;

  before(() => {
    cy.registerUser().then((user) => {
      testUser = user;
    });
  });

  beforeEach(() => {
    cy.clearCookies();
    cy.clearLocalStorage();
    cy.visit("http://localhost:5173/");
  });

  it("logs in successfully with correct credentials", () => {
    cy.get('[data-testid="email-input"]').type(testUser.email);
    cy.get('[data-testid="password-input"]').type(testUser.password);
    cy.get('[data-testid="login-button"]').click();
    cy.url({ timeout: 10000 }).should("include", "/tasks");
  });

  it("shows error with wrong credentials", () => {
    cy.get('[data-testid="email-input"]').type(testUser.email);
    cy.get('[data-testid="password-input"]').type("wrongpass");
    cy.get('[data-testid="login-button"]').click();

    cy.get('[data-testid="login-error"]', { timeout: 10000 })
      .should("exist")
      .and("contain", "Invalid credentials");
  });
});
