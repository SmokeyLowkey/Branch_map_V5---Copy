# Generated by Django 3.2.6 on 2023-09-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0016_userauthentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('Branch_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Corprate', models.TextField()),
                ('Misc', models.TextField()),
                ('Parts', models.TextField()),
                ('Shipping_Info', models.TextField()),
                ('Service', models.TextField()),
                ('Sales', models.TextField()),
            ],
        ),
    ]
