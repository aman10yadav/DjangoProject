from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def homes(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('/signin')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_auth = authenticate(username=username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('/')
            else:
                return redirect("/signin")
        else:
            return render(request, "login.html")
    
def signout(request):
    logout(request)
    return redirect('/signin')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('cnfpassword')
        if password == confirmPassword:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            print("redirecting to signin...")
            return redirect('/signin')
        else:
            return redirect('/signup')
    else:
        return render(request, "signup.html")