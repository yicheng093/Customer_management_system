# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Customers, Employees, Offices, Orderdetails, Orders, Payments, Productlines, Products

# Customers Views
class CustomersListView(ListView):
    model = Customers
    template_name = 'customers_list.html'
    context_object_name = 'customers'
    paginate_by = 10  # 每頁顯示10個客戶

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        return context

class CustomersDetailView(DetailView):
    model = Customers
    template_name = 'orders/customers_detail.html'
    context_object_name = 'customer'

class CustomersCreateView(CreateView):
    model = Customers
    template_name = 'orders/customers_form.html'
    fields = '__all__'
    success_url = reverse_lazy('customers-list')

class CustomersUpdateView(UpdateView):
    model = Customers
    template_name = 'orders/customers_form.html'
    fields = '__all__'
    success_url = reverse_lazy('customers-list')

class CustomersDeleteView(DeleteView):
    model = Customers
    template_name = 'orders/customers_confirm_delete.html'
    success_url = reverse_lazy('customers-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = self.object
        return context

# Employees Views
class EmployeesListView(ListView):
    model = Employees
    template_name = 'orders/employees_list.html'
    context_object_name = 'employees'
    paginate_by = 10  # 每頁顯示10個客戶

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        return context

class EmployeesDetailView(DetailView):
    model = Employees
    template_name = 'orders/employees_detail.html'
    context_object_name = 'employee'

class EmployeesCreateView(CreateView):
    model = Employees
    template_name = 'orders/employees_form.html'
    fields = '__all__'
    success_url = reverse_lazy('employees-list')

class EmployeesUpdateView(UpdateView):
    model = Employees
    template_name = 'orders/employees_form.html'
    fields = '__all__'
    success_url = reverse_lazy('employees-list')

class EmployeesDeleteView(DeleteView):
    model = Employees
    template_name = 'orders/employees_confirm_delete.html'
    success_url = reverse_lazy('employees-list')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['employees'] = self.object
    #     return context
    
    


# Offices Views
class OfficesListView(ListView):
    model = Offices
    template_name = 'orders/offices_list.html'
    context_object_name = 'offices'
    paginate_by = 10  # 每頁顯示10個客戶

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        return context

class OfficesDetailView(DetailView):
    model = Offices
    template_name = 'orders/offices_detail.html'
    context_object_name = 'office'

class OfficesCreateView(CreateView):
    model = Offices
    template_name = 'orders/offices_form.html'
    fields = '__all__'
    success_url = reverse_lazy('offices-list')

class OfficesUpdateView(UpdateView):
    model = Offices
    template_name = 'orders/offices_form.html'
    fields = '__all__'
    success_url = reverse_lazy('offices-list')

class OfficesDeleteView(DeleteView):
    model = Offices
    template_name = 'orders/offices_confirm_delete.html'
    success_url = reverse_lazy('offices-list')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Offices'] = self.object
    #     return context




# 搜尋 Customers
# from django.shortcuts import render
# from .models import Customer

# def customer_list(request):
#     query = request.GET.get('q')
#     if query:
#         customers = Customer.objects.filter(customername__icontains=query)
#     else:
#         customers = Customer.objects.all()
#     return render(request, 'customers_list.html', {'customers': customers})



from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import OrderForm, OrderDetailForm
from .models import Orders, Orderdetails

class IndexView(TemplateView):
    template_name = 'orders/index.html'

# 表單

from orders.forms import OrderDetailFormSet
def create_order(request):
    # OrderDetailFormSet = modelformset_factory(Orderdetails, form=OrderDetailForm, extra=1)
    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_detail_formset = OrderDetailFormSet(request.POST, queryset=Orderdetails.objects.none())
        
        if order_form.is_valid() and order_detail_formset.is_valid():
            order = order_form.save()
            order_details = order_detail_formset.save(commit=False)
            
            for detail in order_details:
                detail.ordernumber = order
                detail.save()
                
            return redirect('order_success')
    else:
        order_form = OrderForm()
        order_detail_formset = OrderDetailFormSet(instance=order_form.instance)
        # order_detail_formset = OrderDetailFormSet(queryset=Orderdetails.objects.none())
    
    context = {
        "hello": "Hello, World!",
        'order_form': order_form,
        'order_detail_formset': order_detail_formset,
    }

    return render(request, 'orders/create_order.html', context)


class create_order_test(CreateView):
    model = Orders
    template_name = 'orders/create_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = OrderDetailFormSet()        
        context["order_form"] = OrderForm()
        context["order_detail_form"] = OrderDetailForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        print("hello")
        formset = context['formset']
        if formset.is_valid():
            print("world")
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

def order_success(request):
    return render(request, 'orders/order_success.html')



# 登入登出
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # 重定向到主頁或其他頁面
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')  # 重定向到主頁或其他頁面

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 註冊成功後重定向到登入頁面
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')  # 重定向到主頁或其他指定頁面

# 處理表單
from django.shortcuts import render, redirect
from .forms import OrderForm, OrderDetailFormSet
from .models import Orders
from datetime import date   

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderDetailFormSet(request.POST)
        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.orderdate = date.today()
            order.save()
            for form in formset:
                order_detail = form.save(commit=False)
                order_detail.ordernumber = order
                order_detail.productcode = form.cleaned_data['productname']
                order_detail.save()
            return redirect('success_page')  # redirect to a success page
    else:
        order_form = OrderForm()
        formset = OrderDetailFormSet()
    
    return render(request, 'orders/create_order.html', {'order_form': order_form, 'formset': formset})


def success_page(request):
    return render(request, 'orders/success_page.html')


# 權限限制存取
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

# @login_required
# def some_view(request):
#     if request.user.groups.filter(name='student').exists():
#         # 用於 student 群組的內容
#         context = {'content': 'This is content for students.'}
#     elif request.user.groups.filter(name='user').exists():
#         # 用於 user 群組的內容
#         context = {'content': 'This is content for users.'}
#     else:
#         # 用於其他使用者的內容
#         context = {'content': 'This is content for other users.'}
    
#     return render(request, 'template_name.html', context)



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def some_view(request):
    context = {}

    if request.user.has_perm('yourapp.can_view_customers'):
        context['show_customers'] = True
    if request.user.has_perm('yourapp.can_view_employees'):
        context['show_employees'] = True
    if request.user.has_perm('yourapp.can_view_offices'):
        context['show_offices'] = True

    return render(request, 'template_name.html', context)
