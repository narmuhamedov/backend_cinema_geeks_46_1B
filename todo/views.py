from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms


# CRUD

# EDIT
def update_todo_view(request, id):
    todo_id = get_object_or_404(models.Todo, id=id)
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Задача успешно изменена')
    else:
        form = forms.TodoForm(instance=todo_id)
    return render(request, template_name='todo/update_todo.html',
                  context={
                      'form': form,
                      'todo_id': todo_id
                  })

# DELETE
def delete_todo_view(request, id):
    drop_todo = get_object_or_404(models.Todo, id=id)
    drop_todo.delete()
    # return redirect('todoList')
    return HttpResponse('Задача успешно удалена')


# READ
def todo_list(request):
    if request.method == 'GET':
        todo_list = models.Todo.objects.filter().order_by('-id')
        return render(request, template_name='todo/todo_list.html',
                      context={'todo_list': todo_list})


# create todo_
def create_todo_view(request):
    if request.method == "POST":
        form = forms.TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todoList')
    else:
        form = forms.TodoForm()
    return render(request, template_name='todo/create_todo.html',
                  context={'form': form})
