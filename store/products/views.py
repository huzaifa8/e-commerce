from django.shortcuts import render


def products_view(request):
    return render(request, 'main.html')
