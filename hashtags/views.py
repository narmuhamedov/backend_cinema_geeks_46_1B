from django.shortcuts import render
from . import models

def all_products_list_view(request):
    if request.method == 'GET':
        products_list = models.Product.objects.filter().order_by('-id')
        context = {'products_list': products_list}
        return render(request, 'all_products_list_view.html',
                      context=context)

def drinks_list_view(request):
    if request.method == 'GET':
        drink = models.Product.objects.filter(tags__name="Напитки").order_by('-id')
        context = {'drink': drink}
        return render(request, 'drink.html',
                      context=context)

def foods_list_view(request):
    if request.method == 'GET':
        foods = models.Product.objects.filter(tags__name="Еда").order_by('-id')
        context = {'foods': foods}
        return render(request, 'foods.html',
                      context=context)


