from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('profile/', views.profile, name="profile" ),
    path('', views.index, name="dashboard"),
    path('error/', views.error, name="error"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('add_profile/', views.add_profile, name="add_profile"),
    path('register/', views.register, name="register"),
]
