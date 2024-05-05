from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  
from django.contrib.auth.views import LogoutView
from django.views import View
from .forms import *

class RegistrationView(View):
    def get(self, request):
        form = CustomerRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:login')  # Redirect to login page after successful registration
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('service_request:home')  # Redirect to home page after successful login
        return render(request, 'login.html',{'form':form})
    
    
class logoutView(LogoutView):
    next_page="customer:login" 