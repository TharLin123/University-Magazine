# Generated by Django 3.2 on 2020-09-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200920_0330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketing_coordinator',
            options={},
        ),
        migrations.AlterModelOptions(
            name='marketing_manager',
            options={},
        ),
        migrations.RemoveField(
            model_name='marketing_coordinator',
            name='name',
        ),
        migrations.RemoveField(
            model_name='marketing_manager',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AlterField(
            model_name='marketing_coordinator',
            name='address',
            field=models.TextField(max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='marketing_coordinator',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='mc_image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='marketing_manager',
            name='address',
            field=models.TextField(max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='marketing_manager',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='mm_image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='student_image', verbose_name='Image'),
        ),
        migrations.AlterModelTable(
            name='marketing_coordinator',
            table='Marketing Coordinator',
        ),
        migrations.AlterModelTable(
            name='marketing_manager',
            table='Marketing Manager',
        ),
    ]
