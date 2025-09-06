#from django.http import HttpResponse
from django.shortcuts import render
from ToDo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False) #can also put .order_by('updated_at / -updated_at')

    complted = Task.objects.filter(is_completed = True)
    print(tasks)
    context = {
        'tasks' : tasks,
        'completed':complted
    }
    return render(request , 'home.html' , context)