# Generated by Django 3.0.3 on 2021-12-28 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midterm_api', '0002_auto_20211228_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='stop',
            new_name='end',
        ),
    ]