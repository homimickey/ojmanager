from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(
        User, verbose_name="user", on_delete=models.CASCADE)
    code_chef_handle = models.CharField(max_length=150)
    hacker_rank_handle = models.CharField(max_length=150, blank=True)
    hacker_earth_handle = models.CharField(max_length=150, blank=True)
    code_forces_handle = models.CharField(max_length=150, blank=True)

    code_chef_score = models.IntegerField(blank=True, default=0)
    hacker_rank_score = models.IntegerField(blank=True, default=0)
    hacker_earth_score = models.IntegerField(blank=True, default=0)
    code_forces_score = models.IntegerField(blank=True, default=0)
    roll_no = models.CharField(max_length=10)
    branch = models.CharField(max_length=4)
    is_blocked = models.BooleanField(default=False)

    @property
    def total_score(self):
        return self.code_chef_score + self.hacker_rank_score + self.hacker_earth_score + self.code_forces_score

    def __str__(self) -> str:
        return self.roll_no
