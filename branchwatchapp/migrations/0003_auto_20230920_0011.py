# Generated by Django 3.2.6 on 2023-09-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0002_alter_companybranch_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybranch',
            name='Branch_ID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='Phone',
            field=models.CharField(max_length=100),
        ),
    ]