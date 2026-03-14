from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('btech/', views.btech, name='btech'),
    path('mba/', views.mba, name='mba'),
    path('diploma/', views.diploma, name='diploma'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
]