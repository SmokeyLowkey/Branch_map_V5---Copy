# Generated by Django 3.2.6 on 2023-09-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0011_auto_20230920_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='companybranch',
            name='Time_Zone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
