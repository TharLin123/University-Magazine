# Generated by Django 3.2 on 2020-09-20 03:30

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200920_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing_Coordinator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('image', models.ImageField(default='default.jpg', upload_to='employer_image', verbose_name='Image')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, verbose_name='Gender')),
                ('dob', models.DateField(null=True, verbose_name='Date of Birth')),
                ('faculty', models.CharField(choices=[('IT', 'Information Technology'), ('BM', 'Business Management'), ('BC', 'Medical Science'), ('ME', 'Mechantronic Engineering'), ('AF', 'Accounting and Financial')], max_length=20, null=True, verbose_name='Choose Faculty')),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='Mobile')),
                ('address', models.CharField(max_length=20, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('object', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Marketing_Manager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('image', models.ImageField(default='default.jpg', upload_to='employer_image', verbose_name='Image')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, verbose_name='Gender')),
                ('dob', models.DateField(null=True, verbose_name='Date of Birth')),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='Mobile')),
                ('address', models.CharField(max_length=20, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('object', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('IT', 'Information Technology'), ('BM', 'Business Management'), ('BC', 'Medical Science'), ('ME', 'Mechantronic Engineering'), ('AF', 'Accounting and Financial')], max_length=20, null=True, verbose_name='Choose Faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Full Name'),
        ),
    ]