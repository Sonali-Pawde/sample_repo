from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from listings.models import Contact
# Create your views here.
def login(request):
    if request.method=="POST":
        #get from values
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            error="Invalid Credentials"
            return render(request, 'accounts/login.html',{'error':error})
    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password2 == password:
            if User.objects.filter(username=username).exists():
                error="Username is already taken."
                return render(request, 'accounts/register.html',{'error':error,'form':request.POST})
            else:
                user_obj=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user_obj.save()
                auth.login(request,user_obj)
                return redirect('index')
        else:
            error="Password do not match."
            return render(request, 'accounts/register.html', {'error': error, 'form': request.POST})
    else:

        return render(request,'accounts/register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    user_id=request.user.id
    contacts=Contact.objects.filter(user_id=user_id).order_by("-contact_date")
    context={
        'contacts':contacts
    }
    return render(request,'accounts/dashboard.html',context)