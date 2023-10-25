from django.contrib import admin
from django.urls import path, include
from .views import usercreateview, currentuserview
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('users/', usercreateview.as_view(), name="user-create"),
    path('login/', obtain_auth_token, name="login"),
    path('users/me/', currentuserview.as_view(), name="current-user") 
]
