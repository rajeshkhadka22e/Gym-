from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from app.models import *
import re


@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username is already taken'})
        
        # Check if passwords match
        if pass1 != pass2:
            return render(request, 'signup.html', {'error': 'Your password and confirm password do not match'})
        
        # Validate the password (minimum length, special character, and uppercase letter)
        if len(pass1) < 8:
            return render(request, 'signup.html', {'error': 'Password must be at least 8 characters long'})
        
        if not any(char.isupper() for char in pass1):
            return render(request, 'signup.html', {'error': 'Password must contain at least one uppercase letter'})
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pass1):
            return render(request, 'signup.html', {'error': 'Password must contain at least one special character'})

        # Create the user
        my_user = User.objects.create_user(username, email, pass1)
        my_user.save()

        # Log the user in immediately after signup
        login(request, my_user)

        # Redirect to home page after successful signup
        return redirect('home')
    
    if request.user.is_authenticated:
        return redirect('home')
    
    return render(request, 'signup.html')
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
        
#         # Check if the username is already taken
#         if User.objects.filter(username=username).exists():
#             return render(request, 'signup.html', {'error': 'Username is already taken'})
        
#         # Check if passwords match
#         if pass1 != pass2:
#             return render(request, 'signup.html', {'error': 'Your password and confirm password do not match'})
        
#         # Create the user
#         my_user = User.objects.create_user(username, email, pass1)
#         my_user.save()
#         return redirect('home')
    
#     if request.user.is_authenticated:
#         return redirect("home")
    
#     return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass1')  # Assuming 'pass1' is the password field

        # Debugging: Print input values to ensure they are correct
        print(f"Email: {email}, Password: {password}")

        # Find the user by email
        try:
            user = User.objects.get(email=email)
            print(f"User found: {user.username}")
        except User.DoesNotExist:
            print("User with this email does not exist.")
            return HttpResponse("Password and email are incorrect")

        # Authenticate using the username and password
        user = authenticate(request, username=user.username, password=password)

        # Debugging: Check if authentication succeeded
        if user is not None:
            print("Authentication successful.")
            login(request, user)
            return redirect('home')  # Corrected redirect
        else:
            print("Authentication failed. Incorrect password.")
            return HttpResponse("Password and email are incorrect")

    if request.user.is_authenticated:
        return redirect("home")
    
    return render(request, 'login.html')



def logout_views(request):
    # Log out the user
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('signup')  # Redirect to the signin page after logging out


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number= request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()
        if len(number) == 10:
            pass
        messages.info(request,"thanks for Contacting us we will get back you soon")
        return redirect('/contact')  
    
    return render(request,"contact.html")


def Enroll(request):
    Menbership = MenbershipPlan.objects.all()
    Trainers = Trainer.objects.all()
    context = {"Menbership":Menbership ,"Trainers":Trainers}
    return render(request,"enroll.html",context)
    
