from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'complete']
        widgets = {
            'title': forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'enter todo item',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter description of todo item'  
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control', 
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'password'  
            })
        }