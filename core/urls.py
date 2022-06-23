from django.urls import path
from . import  views
from .views import DetalharPetView

app_name = 'core'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', DetalharPetView.as_view(), name='detalhar_pet'),
]