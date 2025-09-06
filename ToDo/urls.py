from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/' , views.addTask , name='addTask'),
    path('mark_completed/<int:pk>/' , views.mark_completed , name='mark_completed'),
    path('mark_uncompleted/<int:pk>/' , views.mark_uncompleted , name='mark_uncompleted'),
    path('edit_task/<int:pk>/' , views.edit_task , name='edit_task'),
    path('delete_task/<int:pk>/' , views.delete_task , name='delete_task')
]