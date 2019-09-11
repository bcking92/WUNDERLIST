from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()[::-1]
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    # print("request:", request.POST.get('title'))
    # print("request:", request.POST.get('due_date'))
    title = request.POST.get('title')
    due_date = request.POST.get('due-date')
    if len(title) >= 100:
        return render(request, '형님~~~ 할일이 너~~무나 길어요 100자 이하로 입력해주세요!')
    Todo.objects.create(title=title, due_date=due_date)
    return redirect('todos:index')

def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    context ={
        'todo': todo,
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    due_date = request.POST.get("due-date")
    todo = Todo.objects.get(id=pk)
    todo.title = title
    todo.due_date = due_date
    todo.save()
    return redirect('todos:index')