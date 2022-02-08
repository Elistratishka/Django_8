from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post
from django.forms.widgets import SelectDateWidget


class PostFilter(FilterSet):
    model = Post
    header_filter = CharFilter(field_name='header', lookup_expr='icontains', label='Название')
    author_filter = CharFilter(field_name='author__name__username', lookup_expr='icontains', label='Автор')
    time_filter = DateFilter(field_name='time', lookup_expr='gt', label='Позднее даты', widget=SelectDateWidget)

    class Meta:
        model = Post
        fields = ('header_filter', 'author_filter', 'time_filter')
