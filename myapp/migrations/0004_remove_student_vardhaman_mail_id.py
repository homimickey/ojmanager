# Generated by Django 3.2.6 on 2021-08-08 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210808_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='vardhaman_mail_id',
        ),
    ]