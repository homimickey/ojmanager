from django.urls import path
from .views import  student_list


app_name= "adminsapp"

urlpatterns = [
    path('list/', student_list , name="list" ),
   
]