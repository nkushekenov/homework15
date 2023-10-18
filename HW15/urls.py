from django.urls import path
from . import views  # импорт функции из views.py

urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
]
