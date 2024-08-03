from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
# Create your views here.

def index(request):
    context = {
        'greeting': "Hello! and welcome to Lady Pink's Todo List App to keep you from pulling your hair out and get you organised!!! What are you waiting for? Sign Up Below to join thousands of Pinkies in the organisation frenzy!!",
        'about': "Empower yourself through Lady Pink's Todo App because it allows you to take charge of your own life. Stay organised, stay focused, and achieve your goals with ease! Our app is designed to help you manage your tasks efficiently, giving you more time for what truly matters. Whether you're a student, a professional, or a busy parent, Lady Pink's Todo App is here to simplify your life. Track your progress, set reminders, and never miss a deadline again. Join thousands of Pinkies who have transformed their lives by staying on top of their schedules. With Lady Pink's Todo App, you'll find balance, boost productivity, and achieve more every day. Let's make organization stylish, fun, and incredibly effective!",
        'footer_message': "Show us some love on our social media platforms, get some new inspiration on how to schedule your time effectively and get all the cool features our app has to offer.",
    }

    return render(request, 'Todo/index.html', context)

def update_todo_view(request):
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('update_todo')
    else:
        todo_form = TodoForm()
    
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'Todo/update_todo.html', {
        'todo_form': todo_form,
        'todos': todos
    })
def delete_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('update_todo')