from django.shortcuts import render
from .models import Product
from .filters import Filter



def products_view(request):
    context = Product.objects.all()
    myFilter = Filter(request.GET, queryset=context)
    context = myFilter.qs
    return render(request, 'main.html', {'products': context,
                                         'filter': myFilter})









