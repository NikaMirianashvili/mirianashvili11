from django.urls import path, include
from .views import taskview, categoryview
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', taskview, 'task')
router.register(r'category', categoryview, 'category')

urlpatterns = [
    path('', include(router.urls))
]
