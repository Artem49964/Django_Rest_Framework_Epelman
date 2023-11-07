from django_filters import rest_framework as filters


class AutoParkFilter(filters.FilterSet):
    name_icontains = filters.CharFilter('name', 'icontains')
    name_iendswith = filters.CharFilter('name', 'iendswith')
    name_istartswith = filters.CharFilter('name', 'istartswith')
    name_in = filters.CharFilter('name', 'in')
