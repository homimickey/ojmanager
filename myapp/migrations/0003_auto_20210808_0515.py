# Generated by Django 3.2.6 on 2021-08-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_code_chef_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code_forces_score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='hacker_earth_score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='hacker_rank_score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]