"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from orders.views import (
    CustomersListView, CustomersDetailView, CustomersCreateView, CustomersUpdateView, CustomersDeleteView,
    EmployeesListView, EmployeesDetailView, EmployeesCreateView, EmployeesUpdateView, EmployeesDeleteView,
    OfficesListView, OfficesDetailView, OfficesCreateView, OfficesUpdateView, OfficesDeleteView,IndexView
    # (Add imports for other views)
)
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('customers/', CustomersListView.as_view(), name='customers-list'),
    path('customers/<int:pk>/', CustomersDetailView.as_view(), name='customers-detail'),
    path('customers/create/', CustomersCreateView.as_view(), name='customers-create'),
    path('customers/<int:pk>/update/', CustomersUpdateView.as_view(), name='customers-update'),
    path('customers/<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers-delete'),

    path('employees/', EmployeesListView.as_view(), name='employees-list'),
    path('employees/<int:pk>/', EmployeesDetailView.as_view(), name='employees-detail'),
    path('employees/create/', EmployeesCreateView.as_view(), name='employees-create'),
    path('employees/<int:pk>/update/', EmployeesUpdateView.as_view(), name='employees-update'),
    path('employees/<int:pk>/delete/', EmployeesDeleteView.as_view(), name='employees-delete'),

    path('offices/', OfficesListView.as_view(), name='offices-list'),
    path('offices/<int:pk>/', OfficesDetailView.as_view(), name='offices-detail'),
    path('offices/create/', OfficesCreateView.as_view(), name='offices-create'),
    path('offices/<int:pk>/update/', OfficesUpdateView.as_view(), name='offices-update'),
    path('offices/<int:pk>/delete/', OfficesDeleteView.as_view(), name='offices-delete'),

    path('create_order/', views.create_order_test.as_view(), name='create_order'),
    path('order_success/', views.order_success, name='order_success'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]

