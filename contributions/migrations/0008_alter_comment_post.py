# Generated by Django 3.2 on 2020-10-01 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0007_auto_20201001_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contributions.contribution'),
        ),
    ]
