from django.urls import path
from . import views

urlpatterns = [
    path('outlets/', views.outlet_list, name='outlet-list'),
    path('outlets/<int:pk>/', views.outlet_detail, name='outlet-detail'),
    path('admin/outlets/', views.admin_outlet_list, name='admin-outlet-list'),
    path('admin/outlets/<int:pk>/', views.admin_outlet_detail, name='admin-outlet-detail'),
]
