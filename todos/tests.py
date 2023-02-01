from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todos
# Create your tests here.

class TodosModelsTest(TestCase):
    @classmethod 
    def setUpTestData(cls):
        cls.todo = Todos.objects.create(
            title = "Tập thể dục",
            body = "Tập các bài thể dục"
        )
        
    def test_model_content(self):
        self.assertEqual(self.todo.title, "Tập thể dục")
        self.assertEqual(self.todo.body, "Tập các bài thể dục")
        self.assertEqual(str(self.todo), 'Tập thể dục')
    
    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todos.objects.count(), 1)
        self.assertContains(response, self.todo)
        
    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todos.objects.count(), 1)
        self.assertContains(response, "Tập thể dục")