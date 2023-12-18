# Generated by Django 3.2.6 on 2023-10-03 05:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0019_auto_20230929_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='Corprate',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Misc',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Parts',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Sales',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Service',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Shipping_Info',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='Address',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='Phone',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='WareHouses',
            field=tinymce.models.HTMLField(),
        ),
    ]