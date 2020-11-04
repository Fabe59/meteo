from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.home, name="home"),  #the path for our index view
    path('add/', views.add, name="add"),
    path('delete/', views.delete, name="delete"),
]
