# Generated by Django 4.2.3 on 2023-08-15 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_stcollege_addstudents_scollege_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addstudents',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='addstudents',
            name='total_amount',
        ),
    ]