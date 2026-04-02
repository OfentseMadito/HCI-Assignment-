# report_app/urls.py
from django.urls import path
from . import views

app_name = 'report_app'

urlpatterns = [
    path('', views.report_form, name='home'),
    path('confirmation/<str:reference>/', views.confirmation, name='confirmation'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]