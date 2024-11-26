from django.views import generic
from . import models, forms
from django.http import HttpResponse


class RezkaListView(generic.ListView):
    template_name = "rezka/rezka_list.html"
    context_object_name = "rezka"
    model = models.Rezka
    paginate_by = 10  # Показывать по 5 фильмов на странице

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class RezkaFormView(generic.FormView):
    template_name = "rezka/rezka_form.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("200 OK")
        else:
            return super(RezkaFormView, self).post(request, *args, **kwargs)
