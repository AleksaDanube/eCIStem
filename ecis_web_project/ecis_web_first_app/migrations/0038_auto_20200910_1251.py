# Generated by Django 3.0.3 on 2020-09-10 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecis_web_first_app', '0037_auto_20200824_1905'),
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
        migrations.RemoveField(
            model_name='pfamdb',
            name='genome_ID',
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
