from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Task

class TaskAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task_data = {
            'title': 'Test Task',
            'short_description': 'Test',
            'long_description': 'Test Long Description',
            'due_date': '1970-01-01',
            'priority': 'LOW',
            'status': 'PENDING'
        }
        cls.task = Task.objects.create(**cls.task_data)

    def test_create_task_success(self):
        response = self.client.post('/api/tasks/', self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_task_invalid_data(self):
        invalid_data = self.task_data.copy()
        invalid_data['title'] = ''
        response = self.client.post('/api/tasks/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_task(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        update_data = {'title': 'Updated Title'}
        response = self.client.patch(f'/api/tasks/{self.task.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Title')

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)