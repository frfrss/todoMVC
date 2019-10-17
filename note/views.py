from django.shortcuts import render
from .models import Todo
from django.shortcuts import get_object_or_404, render
from .forms import Todoform
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request,'note/index.html',context)


def vote(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST['todokk']
        todo.save()
        return HttpResponseRedirect(reverse('note:index'))
    else:
        return HttpResponseRedirect(reverse('note:mm'))

def clear(request):
    s = Todo.objects.filter(completed=True).delete()
    return HttpResponseRedirect(reverse('note:index'))










# Create your views here.
