# Generated by Django 3.0.3 on 2020-08-22 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecis_web_first_app', '0025_auto_20200822_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecisdatabase',
            name='clust40pg',
        ),
        migrations.RemoveField(
            model_name='ecisdatabase',
            name='genome_ID_x',
        ),
        migrations.RemoveField(
            model_name='ecisdatabase',
            name='operon_ID',
        ),
        migrations.RemoveField(
            model_name='pfamdb',
            name='gene_id',
        ),
        migrations.DeleteModel(
            name='Clust40PG',
        ),
        migrations.DeleteModel(
            name='EcisDataBase',
        ),
        migrations.DeleteModel(
            name='Operons',
        ),
        migrations.DeleteModel(
            name='PfamDb',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
    ]
