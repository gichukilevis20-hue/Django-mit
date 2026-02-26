from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_student, name='add'),
    path('view/<int:id>/', views.view_student, name='view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
]