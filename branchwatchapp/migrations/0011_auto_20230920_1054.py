# Generated by Django 3.2.6 on 2023-09-20 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0010_auto_20230920_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companybranch',
            old_name='Branch_ID',
            new_name='Branch_Id',
        ),
        migrations.RenameField(
            model_name='companybranch',
            old_name='Branch_name',
            new_name='Branch_Name',
        ),
    ]
