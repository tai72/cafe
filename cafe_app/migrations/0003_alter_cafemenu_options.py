# Generated by Django 4.1.5 on 2023-02-13 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_app', '0002_alter_cafemenu_options_cafemenu_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cafemenu',
            options={'verbose_name_plural': 'Cafe_App'},
        ),
    ]