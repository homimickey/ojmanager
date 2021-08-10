from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
import string
from myapp.models import Student
from faker import Faker
from faker.providers import person

fake = Faker()
fake.add_provider(person)


class Command(BaseCommand):
    help = 'ADDS 100 users and students in the database'

    def handle(self, *args, **kwargs):
        def gen_random_roll_no():
            year = str(random.randint(1, 2)) + str(random.randint(1, 9))
            branch = str(random.randint(1, 5))
            roll = random.choice(string.ascii_uppercase + "123456789")
            no = str(random.randint(1, 9))
            return year + "881A0" + branch + roll + no

        for i in range(100):
            first_name: str = fake.unique.first_name()
            last_name: str = fake.unique.last_name()
            username = first_name.lower() + last_name.lower()
            user: User = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=username + "@vardhaman.org",
            )
            user.set_password("1234!@#$")

            user.save()

            student = Student.objects.create(
                user=user,
                code_chef_handle=username,
                hacker_rank_handle=username,
                hacker_earth_handle=username,
                code_forces_handle=username,
                code_chef_score=random.randint(1, 1000),
                hacker_rank_score=random.randint(1, 1000),
                hacker_earth_score=random.randint(1, 1000),
                code_forces_score=random.randint(1, 1000),
                roll_no=gen_random_roll_no(),
                branch=random.choice(["CSE",
                                      "ECE",
                                      "IT",
                                      "EEE",
                                      "MECH",
                                      "CIVIL"])

            )
            student.save()

        print("done ..")
