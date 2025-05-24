## Exercise 9.2: Manual API Testing

### Testing Tool
- **Postman** (Version 10.18+)

### Test Cases

#### 1. Successful Requests
| Endpoint       | Method | Status Code | Description                     |
|----------------|--------|-------------|---------------------------------|
| `/api/tasks/`  | GET    | 200 OK      | Retrieved all tasks successfully|
| `/api/tasks/`  | POST   | 201 Created | Task created successfully       |

**Example POST Request:**
```json
{
    "title": "Complete documentation",
    "description": "Write API testing docs",
    "status": "pending"
}
