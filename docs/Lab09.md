# Lab 09 - API Testing

## Exercise 9.1: API Endpoint
API endpoint was created using the Django REST API. The serializer is defined at `/core/serializers/task_serializer.py`. The task API can be accessed at /api/tasks/, with individual tasks accessible at /api/tasks/{task_id}. It's hard to visualise this as the Django REST API handles a lot of it in the background.

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
    "title": "Test Task",
    "short_description": "Test",
    "long_description": "Test Long Description",
    "due_date": "1970-01-01",
    "priority": "LOW",
    "status": "PENDING",
}
```

## Exercise 9.3: Automated API Test Cases
`tests/api/test_tasks_api.py`. Running `pytest` will also run this file

## Exercise 9.4: Load & Performance Testing
2 Tests were run with locust and `tests/load/locustfile.py`.

### Results:

#### Constant Load:
`locust -u 100 -r 100 --run-time 1m -f tests/load/locustfile.py --host=http://127.0.0.1:8000/`

![Constant Load](docs/ConstantLoad.png)

There is an inital spike when starting the test as many new users are created.

#### Ramp Up Load:
`locust -u 100 -r 2 --run-time 1m -f tests/load/locustfile.py --host=http://127.0.0.1:8000/`

![Ramp Up Load](docs/RampLoad.png)

The response times are more steady when there isn't a massive increase in users.

### Conclusion:
Running the script on my machine seemed to go well. There was a single failure to delete a task but I have no idea what could've caused that. Getting the list of every task was the slowest obviously, but the median time was only about 10ms higher than a single task modification.