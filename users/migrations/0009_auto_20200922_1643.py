# Generated by Django 3.2 on 2020-09-22 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_faculty_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='Users',
        ),
    ]