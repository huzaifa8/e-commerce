from django.shortcuts import render
from .models import Product
from .filters import Filter


def products_view(request):
    context = Product.objects.all()
    myfilter = Filter(request.GET, queryset=context)
    context = myfilter.qs
    return render(request, 'main.html', {'products': context,
                                         'filter': myfilter})









