from django.contrib import admin
from .models import Customers, Employees, Offices, Orderdetails, Orders, Payments, Productlines, Products
# Register your models here.
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customernumber', 'customername', 'contactlastname', 'contactfirstname', 'phone', 'city', 'country')
    search_fields = ('customername', 'contactlastname', 'contactfirstname', 'phone', 'city', 'country')
    list_filter = ('country', 'city')
    ordering = ('customernumber',)

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employeenumber', 'lastname', 'firstname', 'extension', 'email', 'officecode', 'reportsto', 'jobtitle')
    search_fields = ('lastname', 'firstname', 'email', 'jobtitle')
    list_filter = ('officecode', 'jobtitle')
    ordering = ('employeenumber',)

@admin.register(Offices)
class OfficesAdmin(admin.ModelAdmin):
    list_display = ('officecode', 'city', 'phone', 'addressline1', 'addressline2', 'state', 'country', 'postalcode', 'territory')
    search_fields = ('city', 'country', 'territory')
    list_filter = ('country', 'territory')
    ordering = ('officecode',)

@admin.register(Orderdetails)
class OrderdetailsAdmin(admin.ModelAdmin):
    list_display = ('ordernumber', 'productcode', 'quantityordered', 'priceeach', 'orderlinenumber')
    search_fields = ('ordernumber', 'productcode')
    list_filter = ('ordernumber', 'productcode')
    ordering = ('ordernumber',)
    

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ordernumber', 'orderdate', 'requireddate', 'shippeddate', 'status', 'customernumber')
    search_fields = ('ordernumber', 'status', 'customernumber__customername')
    list_filter = ('status', 'orderdate', 'shippeddate')
    ordering = ('ordernumber',)

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('customernumber', 'checknumber', 'paymentdate', 'amount')
    search_fields = ('customernumber__customername', 'checknumber')
    list_filter = ('paymentdate',)
    ordering = ('customernumber',)

@admin.register(Productlines)
class ProductlinesAdmin(admin.ModelAdmin):
    list_display = ('productline', 'textdescription', 'htmldescription', 'image')
    search_fields = ('productline',)
    ordering = ('productline',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('productcode', 'productname', 'productline', 'productscale', 'productvendor', 'quantityinstock', 'buyprice', 'msrp')
    search_fields = ('productname', 'productvendor', 'productline__productline')
    list_filter = ('productline', 'productvendor')
    ordering = ('productcode',)


