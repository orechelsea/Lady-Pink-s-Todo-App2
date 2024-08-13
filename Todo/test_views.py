from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import TodoForm
from .models import Todo


class UpdateTodoViewTest(TestCase):
     def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username="myUsername", password="myPassword")

        self.todo = Todo.objects.create(
            title="Sample Todo",
            description="This is a sample todo item.",
            priority="medium",
            complete=False,
            user=self.user
        )
    
     def test_update_todo_view_get(self):
        # Test GET request to the update_todo_view
        response = self.client.get(reverse('update_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Todo/update_todo.html')
