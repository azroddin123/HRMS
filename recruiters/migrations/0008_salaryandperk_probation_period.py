# Generated by Django 3.0.3 on 2022-06-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0007_auto_20220611_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryandperk',
            name='probation_period',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
