from django_filters import rest_framework as filters

from .models import *


class BillsFilterSet(filters.FilterSet):
    client_name = filters.CharFilter(field_name='client_name__name')
    client_org = filters.CharFilter(field_name='client_org__name')
   
    class Meta:
        model = Bill
        fields = ('client_name', 'client_org')
