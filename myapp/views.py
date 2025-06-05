from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import AccessCode

# from . forms import UserRegisterForm 


# accounts/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'home/login.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index:dashboard')
    template_name = 'home/register.html'


def index(request):
    if request.method == "POST":
        code = request.POST.get("access_code", "").strip().upper()
        if AccessCode.objects.filter(code=code).exists():
            return redirect('index:access_case', access_code=code)
        messages.error(request, "Invalid access code. Please try again.")
    
    return render(request, 'index.html')


def about(request):
    
    return render(request, 'home/about.html')

def logout(request):
    
    return render(request, 'home/about.html')

def opinion(request):
    
    return render(request, 'opinion.html')

# views.py
# views.py




# def enter_access_code(request):
#     if request.method == "POST":
#         code = request.POST.get("access_code", "").strip().upper()
#         if AccessCode.objects.filter(code=code).exists():
#             return redirect('access_case', access_code=code)
#         messages.error(request, "Invalid access code. Please try again.")
#     return render(request, "enter_code.html")


def access_case(request, access_code):
    code_entry = get_object_or_404(AccessCode, code=access_code.upper())
    case = code_entry.case
    return render(request, 'case_detail.html', {'case': case})