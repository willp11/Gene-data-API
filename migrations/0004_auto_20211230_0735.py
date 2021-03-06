# Generated by Django 3.0.3 on 2021-12-30 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('midterm_api', '0003_auto_20211228_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pfam_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_id', models.CharField(max_length=256)),
                ('domain_description', models.CharField(max_length=256)),
            ],
        ),
        migrations.RenameField(
            model_name='domain',
            old_name='end',
            new_name='stop',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='domain_id',
        ),
        migrations.AddField(
            model_name='domain',
            name='protein',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='midterm_api.Protein'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protein',
            name='taxonomy',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='midterm_api.Organism'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain',
            name='pfam_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='midterm_api.Pfam_id'),
            preserve_default=False,
        ),
    ]
