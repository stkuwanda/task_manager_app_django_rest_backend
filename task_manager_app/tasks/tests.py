from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone


class UserSignupTests(APITestCase):
    def test_user_signup(self):
        url = reverse("signup")
        data = {"username": "testuser",
                "email": "test@example.com", "password": "testpassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def create_task(self):
        url = reverse("task-list")
        data = {"title": "test task", "description": "test desc", "due_date": timezone.now().isoformat(),
                "is_completed": False}
        return self.client.post(url, data, format="json")

    def test_create_task(self):
        response = self.create_task()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        task = Task.objects.latest("id")
        self.assertEqual(task.title, "test task")
        self.assertFalse(task.is_completed)
        self.assertEqual(task.owner, self.user)

    def test_get_task_list(self):
        response = self.create_task()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse("task-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "test task")

    def test_get_task_detail(self):
        response = self.create_task()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.latest("id")

        url = reverse("task-detail", args=[task.id])
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "test task")

    def test_update_task(self):
        response = self.create_task()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.latest("id")
        url = reverse("task-detail", args=[task.id])
        data = {
            "title": "Updated title",
            "description": "Updated desc",
            "due_date": timezone.now().isoformat(),
            "is_completed": True
        }

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = Task.objects.latest("id")
        self.assertEqual(task.title, "Updated title")
        self.assertTrue(task.is_completed)

    def test_delete_task(self):
        response = self.create_task()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.latest("id")
        url = reverse("task-detail", args=[task.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
