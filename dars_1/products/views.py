from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category
import requests
from django.http import HttpResponse

class ProductList(ListView):
    model = Product
    template_name = 'products.html'


def load_products(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        c = Category.objects.create(
            name=item["category"]
        )
        c.save()
        p = Product(
            category=c,
            name=item['title'],
            description=item['description'],
            price=item['price'],
            image=item['image'],
            avalible=item['id'],
        )
        p.save()
    return HttpResponse('ok')
