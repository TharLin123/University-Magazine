# Generated by Django 3.2 on 2020-10-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0010_auto_20201002_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='word_docu',
            field=models.FileField(null=True, upload_to='word_documentation', verbose_name='Word Documentation'),
        ),
    ]
