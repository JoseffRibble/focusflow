import random

from locust import HttpUser, TaskSet, between, task


class TaskAPITasks(TaskSet):
    task_ids = []

    @task
    def create_task_success(self):
        task_data = {
            "title": "Test Task",
            "short_description": "Test",
            "long_description": "Test Long Description",
            "due_date": "1970-01-01",
            "priority": "LOW",
            "status": "PENDING",
        }
        response = self.client.post("api/tasks/", json=task_data)
        if response.status_code == 201:
            task_id = response.json().get("id")
            if task_id is not None:
                TaskAPITasks.task_ids.append(task_id)

    @task
    def get_task_list(self):
        self.client.get("api/tasks/")  # Removed unused assignment

    @task
    def get_single_task(self):
        if TaskAPITasks.task_ids:
            task_id = random.choice(TaskAPITasks.task_ids)
            with self.client.rename_request(f"/api/tasks/{task_id}/"):
                self.client.get(f"api/tasks/{task_id}/")  # Removed unused assignment

    @task
    def update_task(self):
        if TaskAPITasks.task_ids:
            task_id = random.choice(TaskAPITasks.task_ids)
            update_data = {"title": "Updated Title"}
            with self.client.rename_request(f"/api/tasks/{task_id}/"):
                self.client.patch(
                    f"api/tasks/{task_id}/", json=update_data
                )  # Removed unused assignment

    @task
    def delete_task(self):
        if TaskAPITasks.task_ids:
            task_id = random.choice(TaskAPITasks.task_ids)
            with self.client.rename_request(f"/api/tasks/{task_id}/"):
                response = self.client.delete(f"api/tasks/{task_id}/")
            if response.status_code == 204:
                TaskAPITasks.task_ids.remove(task_id)


class TaskAPIUser(HttpUser):
    tasks = [TaskAPITasks]
    wait_time = between(1, 5)
