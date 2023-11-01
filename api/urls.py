from django.contrib import admin
from django.urls import path
from entrance import endpoints as entrance_endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', entrance_endpoints.user_creation, name='create-user'),
]
