from django_filters import rest_framework as filters
from .models import Kurulus


class KurulusFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=Kurulus.KURULUS_TYPE_CHOICES)
    employees_range = filters.RangeFilter(field_name='employees', lookup_expr='range')
    date_range = filters.DateFromToRangeFilter(field_name='date')


    class Meta:
        model = Kurulus
        fields = ['name', 'country', 'type', 'employees_range', 'date_range']