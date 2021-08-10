from django.db.models.query_utils import RegisterLookupMixin
from django.http.request import HttpRequest
from django.shortcuts import render
from myapp.views import Student
from django.db.models import F
# Create your views here.


def student_list(req:HttpRequest):
    year = ""
    platform = ""
    branch = ""
    if("year" in req.GET):
        year = req.GET['year']
        print(year)
    if("platform" in req.GET):
        platform = req.GET['platform']
        print(platform)
    if("branch" in req.GET):
        branch = req.GET['branch']
        print(branch)

    students  = Student.objects.all()

    if year != "":
        roll = str(int(year [-2] + year[-1]) - 4)
        print(roll)
        students = Student.objects.filter(
            roll_no__startswith=roll
        ).annotate(total=F('code_chef_score') + F('code_forces_score') + F('hacker_rank_score') + F('hacker_earth_score')).order_by('-total')
    if platform != "":
        print(year)
        if platform == "CC":
            students = Student.objects.all().order_by('-code_chef_score')[:10]
        elif platform == "CF":
            students = Student.objects.all().order_by('-code_forces_score')[:10]
        elif platform == "HR":
            students = Student.objects.all().order_by('-hacker_rank_score')[:10]
        elif platform == "HE":
            students = Student.objects.all().order_by('-hacker_earth_score')[:10]
        else:
            pass
    print(branch)
    if(branch != ""):
        print(branch)
        students = Student.objects.filter(branch=branch).annotate(total=F('code_chef_score') + F('code_forces_score') + F('hacker_rank_score') + F('hacker_earth_score')).order_by('-total')

    return render(req, "adminsapp/list.html", {"object_list":students})


