# Generated by Django 3.2.6 on 2023-09-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybranch',
            name='Branch_ID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]