from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    email_istartswith = filters.CharFilter('email', 'istartswith')
    email_endswith = filters.CharFilter('email', 'endswith')
    email_icontains = filters.CharFilter('email', 'icontains')
    email_in = filters.BaseInFilter('email')

    name_istartswith = filters.CharFilter('name', 'istartswith')
    name_endswith = filters.CharFilter('name', 'endswith')
    name_icontains = filters.CharFilter('name', 'icontains')
    name_in = filters.BaseInFilter('name')

    surname_istartswith = filters.CharFilter('surname', 'istartswith')
    surname_endswith = filters.CharFilter('surname', 'endswith')
    surname_icontains = filters.CharFilter('surname', 'icontains')
    surname_in = filters.BaseInFilter('surname')

    age_lt = filters.NumberFilter('age', 'lt')
    age_gt = filters.NumberFilter('age', 'gt')
    age_lte = filters.NumberFilter('age', 'lte')
    age_gte = filters.NumberFilter('age', 'gte')
    age_in = filters.BaseInFilter('age')
    age_range = filters.RangeFilter('age')

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id_ASC_DESC'),
            'email',
            'name',
            'surname',
            'age'

        )
    )

