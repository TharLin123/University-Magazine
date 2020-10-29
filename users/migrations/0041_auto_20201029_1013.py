# Generated by Django 3.1.2 on 2020-10-29 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20201029_1005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicyear',
            options={'verbose_name': 'Academic Year', 'verbose_name_plural': 'Academic Year'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Faculty', 'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterModelOptions(
            name='facultyacademicyear',
            options={'verbose_name': 'Faculty Academic Year', 'verbose_name_plural': "Faculties' Academic Years"},
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(choices=[('IT', 'Information Technology'), ('BM', 'Business Management'), ('MS', 'Medical Science'), ('ME', 'Mechantronic Engineering'), ('AF', 'Accounting and Financial')], max_length=50, null=True, unique=True, verbose_name='Faculty Name'),
        ),
        migrations.AlterUniqueTogether(
            name='faculty',
            unique_together=set(),
        ),
        migrations.AlterModelTable(
            name='facultyacademicyear',
            table='Faculty Academic Year',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='academic_year',
        ),
    ]
