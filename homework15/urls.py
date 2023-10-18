from django.contrib import admin
from django.urls import path, include
from HW15 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_data, name='get_data'),
]
