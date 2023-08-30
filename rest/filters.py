from django_filters import rest_framework as filters
from .models import Kurulus


class KurulusFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type', method='filter_type')

    def filter_type(self, queryset, name, value):
        values = value.split(',')
        return queryset.filter(type__in=values)
    
    employees_range_min = filters.NumberFilter(field_name='employees', lookup_expr='gte')
    employees_range_max = filters.NumberFilter(field_name='employees', lookup_expr='lte')
    
    date_range_min = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_range_max = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Kurulus
        fields = ['name', 'country', 'type', 'employees_range_min', 'employees_range_max', 'date_range_min', 'date_range_max']