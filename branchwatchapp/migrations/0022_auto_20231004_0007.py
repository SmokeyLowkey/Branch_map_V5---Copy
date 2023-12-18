# Generated by Django 3.2.6 on 2023-10-04 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchwatchapp', '0021_auto_20231003_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='Corprate',
            new_name='Contacts',
        ),
        migrations.RenameField(
            model_name='companybranch',
            old_name='Address',
            new_name='Info',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='Misc',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='Parts',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='Sales',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='Service',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='Shipping_Info',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Branch_Info',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Branch_Specific_Policies',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Dropbox_Locations_Carriers',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Ordering_Instructions',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Other_Notes',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='Shipping_Instructions',
        ),
        migrations.RemoveField(
            model_name='companybranch',
            name='WareHouses',
        ),
    ]