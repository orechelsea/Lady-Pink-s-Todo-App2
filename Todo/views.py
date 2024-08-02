from django.shortcuts import render
from .models import Todo
# Create your views here.

def index(request):
    context = {
        'greeting': "Hello! and welcome to Lady Pink's Todo List App to keep you from pulling your hair out and get you organised!!! What are you waiting for? Sign Up Below to join thousands of Pinkies in the organisation frenzy!!",
        'about': "Empower yourself through Lady Pink's Todo App because it allows you to take charge of your own life. Stay organised, stay focused, and achieve your goals with ease!",
        'footer_message': "Show us some love on our social media platforms, get some new inspiration on how to schedule your time effectively and get all the cool features our app has to offer.",
    }

    return render(request, 'todo/index.html', context)