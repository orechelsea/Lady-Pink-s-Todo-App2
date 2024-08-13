from django.test import TestCase
from .forms import TodoForm

class TodoFormTest(TestCase):

    def test_form_is_valid_with_complete_checked(self):
        form_data = {
            'title': 'My Task',
            'description': 'This is a valid description.',
            'priority': 'medium',
            'complete': True  
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())  

    def test_form_is_valid_with_complete_unchecked(self):
        form_data = {
            'title': 'My Task',
            'description': 'This is a valid description.',
            'priority': 'medium',
            'complete': False 
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_form_is_invalid_without_title(self):
        form_data = {
            'title': '', 
            'description': 'This is a description.',
            'priority': 'medium',
            'complete': False
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid()) 
        self.assertIn('title', form.errors)