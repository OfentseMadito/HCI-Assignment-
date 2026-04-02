# report_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Report, CATEGORY_CHOICES

# ====================== AUTH VIEWS ======================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('report_app:home')
    else:
        form = UserCreationForm()
    return render(request, 'report_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_app:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'report_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('report_app:home')

# ====================== REPORT VIEWS ======================
def report_form(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description', '')
        location = request.POST.get('location')
        
        report = Report.objects.create(
            category=category,
            description=description,
            location=location,
            user=request.user if request.user.is_authenticated else None
        )
        return redirect('report_app:confirmation', reference=report.reference_number)
    
    context = {'categories': CATEGORY_CHOICES}
    return render(request, 'report_app/report_form.html', context)

def confirmation(request, reference):
    report = Report.objects.get(reference_number=reference)
    context = {'reference_number': report.reference_number}
    return render(request, 'report_app/confirmation.html', context)