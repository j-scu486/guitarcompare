import django_filters
from django_filters import FilterSet, RangeFilter
from .models import GuitarInfo

class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = GuitarInfo
        fields = ['brand_choice']

# class F(FilterSet):
#     price = RangeFilter()

#     class Meta:
#         model = GuitarInfo
#         fields = ['price']