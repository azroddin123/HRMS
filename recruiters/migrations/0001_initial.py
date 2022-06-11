# Generated by Django 3.0.3 on 2022-06-10 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapny_name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_email', models.EmailField(max_length=254)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('no_of_employees', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_designation', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('job_address', models.CharField(blank=True, max_length=200, null=True)),
                ('type_of_work', models.CharField(blank=True, choices=[('full_time', 'full_time'), ('part_time', 'part_time')], default='full_time', max_length=200, null=True)),
                ('no_of_opening', models.CharField(blank=True, max_length=200, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('exp_required', models.CharField(blank=True, max_length=200, null=True)),
                ('probation_period', models.BooleanField(default=True)),
                ('probation_duration', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.Company')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_salary', models.CharField(blank=True, max_length=200, null=True)),
                ('min_salary', models.CharField(blank=True, max_length=200, null=True)),
                ('max_salary', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.JobDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Responsbilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.JobDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Required_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.JobDetail')),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_days_week', models.BooleanField(blank=True, default=False, null=True)),
                ('life_insurence', models.BooleanField(blank=True, default=False, null=True)),
                ('health_insurence', models.BooleanField(blank=True, default=False, null=True)),
                ('dress_code', models.BooleanField(blank=True, default=False, null=True)),
                ('snack_lunch', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.JobDetail')),
            ],
        ),
        migrations.AddField(
            model_name='jobdetail',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiters.RecruiterDetail'),
        ),
    ]
