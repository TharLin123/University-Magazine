# Generated by Django 3.2 on 2020-09-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0004_auto_20200928_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='paragraph',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Paragraph'),
        ),
    ]
