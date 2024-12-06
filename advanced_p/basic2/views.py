from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout  # Import required functions


# Apply CSRF protection on the view
@method_decorator(csrf_protect, name='dispatch')
class RegistrationView(View):
    def get(self, request):
        # Create an empty user form to pass to the template
        form = UserCreationForm()
        return render(request, 'basic2/registration_form.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If form is valid, create the user
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to login page after successful registration
        else:
            # If form is not valid, show error message
            messages.error(request, "Error during registration. Please check the form.")
            return render(request, 'basic2/registration_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')  # Redirect to a home or dashboard page
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'basic2/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # Redirect to the login page

def home_view(request):
    return render(request, 'basic2/home.html')

