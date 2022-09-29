from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by("priority")
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("todos:index")


def read(request):

    return redirect("todos:index")


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if todo.completed == False:
        todo.completed = True
        todo.save()
    else:
        todo.completed = False
        todo.save()
    # content = request.GET.get("content")
    # priority = request.GET.get("priority")
    # deadline = request.GET.get("deadline")

    # todo.content = content
    # todo.priority = priority
    # todo.deadline = deadline

    return redirect("todos:index")


def delete(request, pk):
    # pk 에 해당하는 글 삭제
    Todo.objects.get(id=pk).delete()
    return redirect("todos:index")


def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        "todo": todo,
    }
    return render(request, "todos/edit.html", context)
