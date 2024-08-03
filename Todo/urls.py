from django.urls import path
from . views import update_todo_view, delete_todo_view
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('update/', update_todo_view, name='update_todo'),
    path('delete/<int:todo_id>/', delete_todo_view, name='delete_todo'),
]