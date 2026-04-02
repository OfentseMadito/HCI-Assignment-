# dashboard_app/urls.py
from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
]