from django.urls import path
from . views import update_todo_view, delete_todo_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_todo/', views.update_todo_view, name='update_todo'),
    path('update_todo/<int:todo_id>/', views.update_todo_view, name='update_todo'),
    path('update_todo_complete/<int:todo_id>/', views.update_todo_complete, name='update_todo_complete'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_view, name='delete_todo'),
]