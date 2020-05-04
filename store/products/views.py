from django.shortcuts import render
from .models import Product


def products_view(request):
    context = Product.objects.all()
    return render(request, 'main.html', {'products': context})

