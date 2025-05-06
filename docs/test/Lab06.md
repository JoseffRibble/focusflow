# Exercise 6 – Mock Testing 

- This document summarizes the design and implementation for Exercises 6.1 to 6.4, covering model-level testing, service abstraction, repository encapsulation, and REST API development.
- All documentation was reviewed using ChatGPT to ensure grammatical accuracy.

## 6.1 – Unit Testing of Models

### Test Design Techniques Applied

As part of our testing strategy for FocusFlow models, we applied the following test design methods:

- **Equivalence Class Partitioning**
  - Valid vs. invalid email formats
  - Valid vs. short or empty passwords
  - Assigning a task to a user vs. assigning to a nonexistent user

- **Boundary Value Analysis**
  - Minimum length password (6 characters)
  - Empty string fields (task title, team name)
  - Due date field being required

- **Decision Table Testing**
  - A task can only be assigned to either a user or a team, not both.
  - Assigning to one automatically unassigns the other.
  - If neither is assigned, the task remains unassigned.
  - These conditions were verified through explicit test cases in [test_models.py](../../tests/models/test_models.py).

### Test Additions

We extended the model unit tests with the following scenarios:
- Email format validation using Django’s built-in validators
- Password validation (empty, too short)
- Creating tasks with missing required fields
- Task assignment mutual exclusion logic
- Creating valid user, team, and task entities
- User-task permission logic (via other test files)

## 6.2 – Service Testing

### Implemented Service: `UserService`
- Handles registration, login, role assignment, team join/leave.

### Testing Strategy
- Mocked `UserRepository` to isolate logic.
- Tested both positive and negative flows:
  - Duplicate email
  - Invalid password
  - Nonexistent user
- Tests grouped logically by feature (registration, login, role, team).

## 6.3 – Repository Testing

### Repository: `UserRepository`

| Method | Description |
|--------|-------------|
| `create()`             | Create user instance |
| `find_by_id()`         | Find user by ID |
| `find_by_email()`      | Find user by email |
| `update()`             | Update user fields |
| `delete()`             | Delete user |
| `find_by_role()`       | Filter users by role |
| `find_by_team()`       | Filter users in a team |

### Testing Details
- Used in-memory SQLite via `pytest.mark.django_db`
- Repository methods tested in isolation
- Each method validated for correct behavior and persistence
- Role field added to `User` model to support filtering

## 6.4 – REST API Controller

### Implemented Endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/register`         | User registration |
| POST   | `/api/users/<id>/role`  | Assign user role |
| CRUD   | `/api/teams/`           | Team management |

### Architecture:
- Built using Django REST Framework (`APIView`, `ViewSet`)
- Input validation with serializers
- Named routes used for reverse resolution
- Centralized error handling and 4xx status codes

### Testing Coverage:
- API views tested with `APIClient`
- Serializers tested independently for validation and output
- Status codes and persistence assertions included
