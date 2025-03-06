from django.shortcuts import render,redirect
from .models import Users
from django.contrib.auth.models import User
from django.contrib import messages  # ✅ Import messages

from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login as auth_login

#LOGIN  
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=User.objects.get(email=email)
            if check_password(password,user.password):
                auth_login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'Invalid Password'})
        except Users.DoesNotExist:
            return render(request,'login.html',{'error':'Email dos not exist'})
    else:
        return render(request,'login.html')
    
#register
def register(request):
    if request.method == 'POST':
        username = request.POST.get('name', '').strip()  
        
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email or not password:
            messages.error(request, "All fields are required!")
            return render(request, 'register.html')

        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered! Please log in.")
            return redirect('login')

        
        user = User.objects.create(username=username, email=email, password=make_password(password))
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')
    
def home(request):
    return render(request, 'home.html')  # Show home page after login

def cart(request):
    return render(request, 'cart.html')  # Show cart page only if user clicks

    



    
        




