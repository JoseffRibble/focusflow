from core.models import Task, User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class TaskAPITests(APITestCase):
    @classmethod
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass123"
        )
        cls.token = str(RefreshToken.for_user(cls.user).access_token)

        # Initialize a task for testing
        cls.task = Task.objects.create(
            title="Test Task",
            short_description="Short",
            long_description="Long",
            due_date="2025-12-31",
            priority="HIGH",
            assignee_user=cls.user,
        )

        cls.task_data = {
            "title": "New Task",
            "short_description": "Short",
            "long_description": "Long",
            "due_date": "2025-12-31",
            "priority": "HIGH",
        }

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_create_task_success(self):
        response = self.client.post("/api/tasks/", self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_task_invalid_data(self):
        invalid_data = self.task_data.copy()
        invalid_data["title"] = ""
        response = self.client.post("/api/tasks/", invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_task_list(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_task(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)

    def test_update_task(self):
        update_data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/tasks/{self.task.id}/", update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Title")

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
