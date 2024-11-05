from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# film_list
def films_list_view(request):
    if request.method == 'GET':
        film_list = models.Films.objects.filter().order_by('-id')
        context = {'film_list': film_list}
        return render(request, template_name='show.html', context=context)


# detail film
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Films, id=id)
        context = {'film_id': film_id}
        return render(request, template_name='show_detail.html', context=context)




def first_lesson_django(request):
    if request.method == 'GET':
        return HttpResponse('🐍Hello DJANGO TEMPLATES 🐍')


def picture_view(request):
    if request.method == 'GET':
        return HttpResponse("<img src = 'https://itproger.com/img/news/1592990176.jpg'  >")
