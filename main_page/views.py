from django.shortcuts import render
from django.http import HttpResponse


def first_lesson_django(request):
    if request.method == 'GET':
        return HttpResponse('🐍Hello DJANGO TEMPLATES 🐍')


def picture_view(request):
    if request.method == 'GET':
        return HttpResponse("<img src = 'https://itproger.com/img/news/1592990176.jpg'  >")
