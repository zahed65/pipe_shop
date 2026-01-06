from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sample/', views.sample_view, name='sample'),
    path('contact/', views.contact, name='contact'),
]
