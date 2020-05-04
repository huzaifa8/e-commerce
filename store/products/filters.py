import django_filters
from .models import Product


class Filter(django_filters.FilterSet):
    django_filters.CharFilter(label='Article')

    class Meta:
        model = Product
        fields = {
            'name': ['icontains']
            # 'brand': ['icontains']
        }