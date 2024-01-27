from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import File
from app.forms import LoginForm


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login_page.html", {"form": form})


def homepage(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        return redirect("dashboard")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    files = File.objects.all().order_by("-upload_date")
    payload = {"files": files}
    return render(request, "dashboard.html", payload)


def logout_view(request):
    logout(request)
    return redirect("/")
