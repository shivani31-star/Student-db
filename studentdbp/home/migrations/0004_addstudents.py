# Generated by Django 4.2.3 on 2023-07-31 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_addcourses_delete_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(blank=True, max_length=100, null=True)),
                ('semail', models.EmailField(max_length=100)),
                ('smobile', models.CharField(max_length=10)),
                ('saddress', models.CharField(max_length=255)),
                ('sdegree', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('due_amount', models.FloatField()),
                ('scourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.addcourses')),
            ],
        ),
    ]
