from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializer import taskserializer, categoryserializer
from .models import Task, Category
from .pagination import taskspagination
from .filters import taskfilter
# Create your views here.

class taskview(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = taskserializer
    pagination_class = taskspagination
    filterset_class = taskfilter

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class categoryview(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoryserializer


