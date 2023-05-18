from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists try another username")
            return redirect('signup')
        elif not username.isalnum():
            messages.error(request,"username must be alpha-numeric")
            return redirect("signup")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exists try another email")
            return redirect("signup")
        elif len(password)<8:
            messages.error("password must contain more than 8 characters")
            return redirect("signup")
        elif password!=password2:
            messages.error(request,"password does not match")
        else:
            myuser=User(username=username,email=email,password=password)
            myuser.set_password(password)
            myuser.save()
            messages.success(request,"Your account has been has been successfully created. ")

            return redirect('signin')

    return render(request,'accounts/signup.html')


def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser == True:
                messages.success(request,'You are logged in')
                return redirect('home')
                
                # return render(request,'vehicle/superuser.html')

            elif user.is_superuser == False and user.user_type == 'admin_user':
                messages.success(request,'You are logged in')
                
                return redirect('home')
                # return render(request,'vehicle/adminuser.html')
            else:
                messages.success(request,'You are logged in')
                
                return redirect('home')
                # return render(request,'vehicle/normaluser.html')
        else:
            messages.error(request,"invalid credentials")
            return redirect('signin')

    return render(request,'accounts/login.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request,"You are logouted")
    return redirect('signin')


# super user can only add admin user
#this is for  admin user registration

@login_required(login_url='signin')
def admin_register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists try another username")
            return redirect('register')
        elif not username.isalnum():
            messages.error(request,"username must be alpha-numeric")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exists try another email")
            return redirect("register")
        elif len(password)<8:
            messages.error("password must contain more than 8 characters")
            return redirect("register")
        elif password!=password2:
            messages.error(request,"password does not match")
        else:
            myuser=User(username=username,email=email,password=password)
            myuser.set_password(password)
            myuser.user_type='admin_user'
            myuser.save()
            messages.success(request,"Your account has been has been successfully created. ")

            return redirect('home')

    return render(request,'accounts/register.html')

