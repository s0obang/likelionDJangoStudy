from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todolist.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'tododetail.html', {'todo': todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todopost.html', {'form': form})


def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todopost.html', {'form': form})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect('todo:todo_list')

def todo_discard(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = False
    todo.save()
    return redirect('todo:todo_done_list')


def todo_done_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, 'tododonelist.html', {'dones': dones})