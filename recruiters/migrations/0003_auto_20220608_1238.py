# Generated by Django 3.0.3 on 2022-06-08 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0002_auto_20220608_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='creted_by',
            new_name='created_by',
        ),
    ]
