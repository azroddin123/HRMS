# Generated by Django 3.0.3 on 2022-06-13 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruiters', '0008_salaryandperk_probation_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='required_skill',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
