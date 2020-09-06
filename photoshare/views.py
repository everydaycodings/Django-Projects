from django.shortcuts import render, HttpResponse, redirect
from .models import Suscribe, ContactUs, Addpost
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def index(request):
    if request.method == "POST" and "suscribe" in request.POST:
        email = request.POST['email']
        inst =  Suscribe(email=email)

        if len(email) < 5 or email == "":
            messages.error(request, "Error, Please Give your Valid Email!!!")
        else:
            inst.save()
            messages.success(request, "Success, Your Message Has Been Successfully Sent To The Subscription List :) ")
    
    elif request.method == "POST" and "contactus" in request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contactus = ContactUs(name=name, email=email, message=message)

        if len(email) < 5 or len(name) < 2 or len(message) < 5:
            messages.error(request, "Error, Please Enter The Valid Information!!!")
        
        else:
            contactus.save()
            messages.success(request, "Success, Your Message Has Been Successfully Sent To The Admin :) ")


    posts = Addpost.objects.order_by("-id")[:3]

    context = {"posts": posts}

    return render(request, "photoshare/index.html", context)


@login_required(login_url="login")
def gallary(request):

    posts = Addpost.objects.order_by("-id")

    context = {"posts": posts} 

    return render(request, "photoshare/gallary.html", context)


@login_required(login_url="login")
def addpost(request):

    context = {}
    
    if request.method == "POST":
        username = request.user
        pic = request.FILES["pic"]
        title = request.POST["title"]
        
        if len(title) < 5:
            messages.error(request, "Error, Please Give a Valid username or Title must be minimum 10 words!")
        else:
            info = Addpost(username=username, img=pic, title=title)
            info.save()
            messages.success(request, "Success, Your Post have been posted to Gallary Section")
    
        context = {"username": username}
    
    return render(request, "photoshare/submit_forms.html", context)


@login_required(login_url="login")
def contact(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contactus = ContactUs(name=name, email=email, message=message)
        contactus.save()

    return render(request, "photoshare/contact.html")


def loginpage(request):

    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
        
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Username OR Password is incorrect")
            

    return render(request, "photoshare/login.html")


def signup(request):

    if request.user.is_authenticated:
        return redirect("index")

    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Success, Your Account has been Sucessfully Created Now You Can Login")
                return redirect("login")

    context = {"form": form}

    return render(request, "photoshare/signup.html", context)


def logoutUser(request):

    logout(request)


    return redirect("login")