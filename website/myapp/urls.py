
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about, name='about'),
    path('create', views.create, name='create')
]