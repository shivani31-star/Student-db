# Generated by Django 4.2.3 on 2023-08-01 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_addstudents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addstudents',
            old_name='saddress',
            new_name='stcollege',
        ),
        migrations.RenameField(
            model_name='addstudents',
            old_name='scourse',
            new_name='stcourse',
        ),
        migrations.RenameField(
            model_name='addstudents',
            old_name='sdegree',
            new_name='stdegree',
        ),
        migrations.RenameField(
            model_name='addstudents',
            old_name='semail',
            new_name='stemail',
        ),
        migrations.RenameField(
            model_name='addstudents',
            old_name='smobile',
            new_name='stmobile',
        ),
        migrations.RenameField(
            model_name='addstudents',
            old_name='sname',
            new_name='stname',
        ),
    ]
