# Generated by Django 3.0.3 on 2022-06-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0002_auto_20220611_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetail',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
