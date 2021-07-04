from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('linearview/', views.linearview, name='linearview'),
    path('binaryview/', views.binaryview, name='binaryview'),
    path('bubblesortview/', views.bubblesortview, name='bubblesortview'),
    path('mergesortview/', views.mergesortview, name='mergesortview'),
    path('insertionsortview/', views.insertionsortview, name='insertionsortview'),
    path('selectionsortview/', views.selectionsortview, name='selectionsortview'),
    path('stackview/', views.stackview, name='stackview'),
    path('sort', views.sort, name='sort'),
    path('search', views.search, name='search'),


]