# Generated by Django 3.0.3 on 2021-12-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midterm_api', '0007_auto_20211230_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organism',
            name='id',
        ),
        migrations.AlterField(
            model_name='organism',
            name='taxa_id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
    ]
