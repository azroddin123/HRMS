# Generated by Django 3.0.3 on 2022-06-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0003_jobdetail_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetail',
            name='key_resposibilities',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]