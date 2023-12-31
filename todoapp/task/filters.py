import django_filters
from .models import Task


class taskfilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta: 
        model = Task
        fields = ['completed', 'title']