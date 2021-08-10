from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.db.models import F
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm, UserForm, StudentForm
from .models import Student


# Create your views here.
def leaderboard(req: HttpRequest):
    if not req.user.is_authenticated:
        return redirect('myapp:login')

    student: Student = Student.objects.get(user=req.user)
    students = Student.objects.filter(
        roll_no__startswith=student.roll_no[:2]
    ).annotate(total=F('code_chef_score') + F('code_forces_score') + F('hacker_rank_score') + F('hacker_earth_score')).order_by('-total')[:10]
    

    return render(req, "myapp/leaderboard.html", {"student": student, "students": students})


def index(req: HttpRequest):
    if not req.user.is_authenticated:
        return redirect('myapp:login')

    student: Student = Student.objects.get(user=req.user)

    return render(req, "myapp/dashboard.html", {"student": student})


def profile(req: HttpRequest):
    if not req.user.is_authenticated:
        return redirect('myapp:login')

    student = Student.objects.get(user=req.user)
    all_filled = False

    if(student.code_chef_handle == "" or student.code_forces_handle == "" or student.hacker_rank_handle == "" or student.hacker_earth_handle == ""):
        all_filled = True
    return render(req, "myapp/profile.html", {"student": student, "all_filled": all_filled})


def error(req):
    return render(req, "myapp/404.html")



def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, "myapp/login.html", {"form": LoginForm})
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("myapp:dashboard")
        else:
            return render(request, "myapp/login.html", {"form": LoginForm(request.POST)})


def add_profile(request: HttpRequest):
    platform = request.POST.get("platform")
    handle = request.POST.get("handle")
    if not request.user.is_authenticated:
        return redirect('myapp:login')

    student: Student = Student.objects.get(user=request.user)

    if(platform == "Code Forces"):
        student.code_forces_handle = handle
        student.save(update_fields=["code_forces_handle"])
    elif(platform == "Hacker Rank"):
        student.hacker_rank_handle = handle
        student.save(update_fields=["hacker_rank_handle"])
    elif(platform == "Hacker Earth"):
        student.hacker_earth_handle = handle
        student.save(update_fields=["hacker_earth_handle"])

    return redirect("myapp:profile")


def logout(req):
    auth_logout(req)
    return redirect("myapp:login")



def register(req :HttpRequest):
    if req.method == 'GET':
        user_form = UserForm()
        student_form = StudentForm()
        return render(req, "myapp/register.html")
    if req.method == 'POST':
        user_form = UserForm(req.POST)
        student_form = StudentForm(req.POST)
        if user_form.is_valid() and student_form.is_valid():
            # TODO save models

            user = User.objects.create(**user_form.cleaned_data)
            user.save()

            auth_login(req, user)

            student = Student.objects.create(
                user = user, 
                code_chef_handle = student_form.cleaned_data["code_chef_handle"], 
                code_forces_handle = student_form.cleaned_data["code_forces_handle"],
                hacker_rank_handle = student_form.cleaned_data["hacker_rank_handle"],
                hacker_earth_handle = student_form.cleaned_data["hacker_earth_handle"],
                roll_no = student_form.cleaned_data["roll_no"]
            )

            student.save()
            
            return redirect("myapp:dashboard")
        
        else:
            print(student_form.is_valid())
            print(student_form.errors)
            print(user_form.is_valid())

            context  = {
                "user_form":user_form,
                "student_form":student_form

            }
            return render(req, "myapp/register.html", context )