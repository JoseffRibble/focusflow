from locust import HttpUser, TaskSet, task, between
import random

class TaskAPITasks(TaskSet):
    task_ids = []  # List to keep track of created task IDs

    # Task Creation
    @task
    def create_task_success(self):
        task_data = {
            'title': 'Test Task',
            'short_description': 'Test',
            'long_description': 'Test Long Description',
            'due_date': '1970-01-01',
            'priority': 'LOW',
            'status': 'PENDING'
        }
        response = self.client.post("api/tasks/", json=task_data)
        if response.status_code == 201:  # Assuming 201 is returned on successful creation
            task_id = response.json().get('id')  # Get the ID of the created task
            if task_id is not None:
                TaskAPITasks.task_ids.append(task_id)  # Add the task ID to the list

    # Task Retrieval
    @task
    def get_task_list(self):
        response = self.client.get("api/tasks/")

    @task
    def get_single_task(self):
        if TaskAPITasks.task_ids:  # Check if there are any tasks created
            task_id = random.choice(TaskAPITasks.task_ids)  # Select a random valid task ID
            with self.client.rename_request(f"/api/tasks/{task_id}/"):
                response = self.client.get(f"api/tasks/{task_id}/")

    # Task Update
    @task
    def update_task(self):
        if TaskAPITasks.task_ids:  # Check if there are any tasks created
            task_id = random.choice(TaskAPITasks.task_ids)  # Select a random valid task ID
            update_data = {'title': 'Updated Title'}
            with self.client.rename_request(f"/api/tasks/{task_id}/"):
                response = self.client.patch(f"api/tasks/{task_id}/", json=update_data)

    # Task Deletion
    @task
    def delete_task(self):
        if TaskAPITasks.task_ids:  # Check if there are any tasks created
            task_id = random.choice(TaskAPITasks.task_ids)  # Select a random valid task ID
            with self.client.rename_request(f"/api/tasks/{task_id}/"):
                response = self.client.delete(f"api/tasks/{task_id}/")
            if response.status_code == 204:
                TaskAPITasks.task_ids.remove(task_id)  # Remove the ID from the list if deleted successfully

class TaskAPIUser(HttpUser):
    tasks = [TaskAPITasks]
    wait_time = between(1, 5)
