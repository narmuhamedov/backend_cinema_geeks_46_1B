from todo.models import Todo
from todo.forms import TodoForm
from django.shortcuts import get_object_or_404
from django.views import generic

class TodoListView(generic.ListView):
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'
    model = Todo

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class CreateTodoView(generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = TodoForm
    success_url = '/todo_class/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)


class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = TodoForm
    success_url = '/todo_class/'


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Todo, id=todo_id)

class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_class/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Todo, id=todo_id)
