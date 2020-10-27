# Generated by Django 3.1.2 on 2020-10-25 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_guest_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
                'db_table': 'Admin',
            },
            bases=('users.user',),
        ),
        migrations.AddField(
            model_name='faculty',
            name='academic_year',
            field=models.CharField(choices=[('IT', 'Information Technology'), ('BM', 'Business Management'), ('MS', 'Medical Science'), ('ME', 'Mechantronic Engineering'), ('AF', 'Accounting and Financial')], max_length=50, null=True, unique=True, verbose_name='Faculty Name'),
        ),
    ]