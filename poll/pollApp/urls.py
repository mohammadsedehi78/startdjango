from django.urls import path
from pollApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
