# Generated by Django 3.2.6 on 2023-09-20 05:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyBranch',
            fields=[
                ('Branch_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Branch_name', models.CharField(max_length=100)),
                ('WareHouses', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('Phone', models.CharField(max_length=20)),
                ('Branch_Info', models.TextField()),
                ('Shipping_Instructions', models.TextField()),
                ('Ordering_Instructions', models.TextField()),
                ('Branch_specific_policies', models.TextField()),
                ('Dropbox_Locations_carriers', models.TextField()),
                ('Other_Notes', models.TextField()),
                ('Geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'CompanyBranch',
            },
        ),
    ]
