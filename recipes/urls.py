from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borscht/', views.borscht, name='borscht'),
    path('burger/', views.burger, name='burger'),
    path('steak/', views.steak, name='steak'),
]
