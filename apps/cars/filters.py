from django_filters import rest_framework as filters

from .choices.body_type_choices import BodyTypeChoices


class CarFilter(filters.FilterSet):
    brand_istartswith = filters.CharFilter('brand', 'istartswith')
    brand_endswith = filters.CharFilter('brand', 'endswith')
    brand_icontains = filters.CharFilter('brand', 'icontains')
    brand_in = filters.BaseInFilter('brand')

    price_lt = filters.NumberFilter('price', 'lt')
    price_gt = filters.NumberFilter('price', 'gt')
    price_lte = filters.NumberFilter('price', 'lte')
    price_gte = filters.NumberFilter('price', 'gte')
    price_in = filters.BaseInFilter('price')
    price_range = filters.RangeFilter('price')

    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    year_lte = filters.NumberFilter('year', 'lte')
    year_gte = filters.NumberFilter('year', 'gte')
    year_in = filters.BaseInFilter('year')
    year_range = filters.RangeFilter('year')

    body = filters.ChoiceFilter('body', choices=BodyTypeChoices.choices)

    order = filters.OrderingFilter(
        fields=(
            ('id','id_ASC_DESC'),
            'brand',
            'price',
            'year',

        )
    )
