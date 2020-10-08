# Generated by Django 3.2 on 2020-09-22 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200921_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('IT', 'Information Technology'), ('BM', 'Business Management'), ('MS', 'Medical Science'), ('ME', 'Mechantronic Engineering'), ('AF', 'Accounting and Financial')], max_length=50, null=True, verbose_name='Faculty Name')),
                ('closure_date', models.DateField(null=True, verbose_name='Closure Date')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.AlterModelOptions(
            name='marketing_coordinator',
            options={'verbose_name': 'Marketing Coordinator', 'verbose_name_plural': 'Marketing Coordinators'},
        ),
        migrations.AlterModelOptions(
            name='marketing_manager',
            options={'verbose_name': 'Marketing Manager', 'verbose_name_plural': 'Marketing Managers'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_marketing_coordinator',
            field=models.BooleanField(default=False, verbose_name='Marketing Coordinator'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_marketing_manager',
            field=models.BooleanField(default=False, verbose_name='Marketing Manager'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='marketing_coordinator',
            name='faculty',
            field=models.OneToOneField(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.faculty', verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.OneToOneField(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.faculty', verbose_name='Faculty'),
        ),
    ]