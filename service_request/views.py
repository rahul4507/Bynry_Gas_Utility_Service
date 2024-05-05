from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  
from .forms import ServiceRequestForm
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def home(request):
    sr = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'home.html', {'service_requests': sr})

@login_required
def service_request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request=request)  # Pass request object to the form
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('service_request:home')
    else:
        form = ServiceRequestForm(request=request)  # Pass request object to the form
    return render(request, 'create.html', {'form': form})