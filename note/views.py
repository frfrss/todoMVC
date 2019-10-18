from django.shortcuts import render
from .models import Todo
from django.shortcuts import get_object_or_404, render
from .forms import Todoform
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt

def indexf(request):
    stodo = Todo.objects.all()
    todos = []
    if stodo:
        for i in range(len(stodo)):
            stodo[i].todo_id = i
            todo = {
                'id': i,
                'title': stodo[i].title,
                'completed': stodo[i].completed
            }
            todo = json.dumps(todo)
            todos.append(todo)
    context = {'todos':todos}
    return render(request,'note/index.html',context)


def refresh():
    todos = Todo.objects.all()
    if todos:
        for i in range(len(todos)):
            todos[i].todo_id = i
    return HttpResponse()


@csrf_exempt
def save_todo(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = json.loads(request.body, encoding='utf-8')['title']
        todo.todo_id = json.loads(request.body, encoding='utf-8')['id']
        todo.completed = json.loads(request.body, encoding='utf-8')['completed']
        todo.save()
    #     return HttpResponseRedirect(reverse('note:index'))
    # else:
    #     return HttpResponseRedirect(reverse('note:index'))
    return refresh()



@csrf_exempt
def delete(request):
    if request.method == 'POST':
        todos = Todo.objects.all()
        if len(todos) == 1:
            Todo.objects.all().delete()
        else:
            todo_id = int(json.loads(request.body)['id'])
            todo = Todo.objects.get(todo_id=todo_id)
            todo.delete()
    #     return HttpResponseRedirect(reverse('note:index'))
    # else:
    #     return HttpResponseRedirect(reverse('note:index'))
    return refresh()

@csrf_exempt
def tick(request):
    if request.method == 'POST':
        if len(Todo.objects.all()) == 1:
            todo = Todo.objects.all()[0]
        else:
            temp_id = int(json.loads(request.body)['id'])
            todo = Todo.objects.get(todo_id=temp_id)
        if todo:
            todo.completed = json.loads(request.body)['completed']
            todo.save()
        return refresh()

@csrf_exempt
def rm(request):
    todos = Todo.objects.filter(completed=True)
    if todos:
        for todo in todos:
            todo.delete()
    return refresh()


@csrf_exempt
def change(request):
    if request.method == 'POST':
        temp_id = int(json.loads(request.body)['id'])
        todo = Todo.objects.get(todo_id=temp_id)
        todo.title = json.loads(request.body)['title']
        todo.save()
    return refresh()










# Create your views here.
