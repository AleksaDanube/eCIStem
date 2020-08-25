# Generated by Django 3.0.3 on 2020-08-02 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecis_web_first_app', '0005_clust40pg_ecisdatabase_operons_species'),
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
            name='Species',
        ),
    ]
