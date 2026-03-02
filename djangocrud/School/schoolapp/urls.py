from django.urls import path
from . import views
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm    

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_student, name='add'),
    path('view/<int:id>/', views.view_student, name='view'),
    path('edit/<int:id>/', views.update_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
]
