from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('linearview/', views.linearview, name='linearview'),
    path('binaryview/', views.binaryview, name='binaryview'),
    path('getele/', views.getelement, name='elem'),
    path('sort', views.sort, name='sort'),
    path('search', views.search, name='search'),



]