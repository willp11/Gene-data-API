# Generated by Django 3.0.3 on 2021-12-30 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('midterm_api', '0006_auto_20211230_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='protein',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='domains', to='midterm_api.Protein'),
        ),
        migrations.DeleteModel(
            name='ProteinDomainAssignment',
        ),
    ]
