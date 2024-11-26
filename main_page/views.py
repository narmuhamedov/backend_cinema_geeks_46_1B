from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models


# Search button
class SearchView(generic.ListView):
    template_name = "show.html"
    context_object_name = "film_list"
    paginate_by = 5

    def get_queryset(self):
        return models.Films.objects.filter(
            title__icontains=self.request.GET.get("q")
        ).order_by("-id")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# # film_list
@method_decorator(cache_page(60 * 15), name="dispatch")
class FilmListView(generic.ListView):
    template_name = "show.html"
    context_object_name = "film_list"
    model = models.Films

    def get_queryset(self):
        return self.model.objects.select_related().order_by("-id")


# def films_list_view(request):
#     if request.method == 'GET':
#         film_list = models.Films.objects.filter().order_by('-id')
#         context = {'film_list': film_list}
#         return render(request, template_name='show.html', context=context)


# detail film
class FilmDetailView(generic.DetailView):
    template_name = "show_detail.html"
    context_object_name = "film_id"

    def get_object(self, **kwargs):
        film_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=film_id)


# def film_detail_view(request, id):
#     if request.method == 'GET':
#         film_id = get_object_or_404(models.Films, id=id)
#         context = {'film_id': film_id}
#         return render(request, template_name='show_detail.html', context=context)


def first_lesson_django(request):
    if request.method == "GET":
        return HttpResponse("🐍Hello DJANGO TEMPLATES 🐍")


def picture_view(request):
    if request.method == "GET":
        return HttpResponse(
            "<img src = 'https://itproger.com/img/news/1592990176.jpg'  >"
        )
