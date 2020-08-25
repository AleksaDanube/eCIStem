# Generated by Django 3.0.3 on 2020-07-04 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecis_web_first_app', '0002_auto_20200704_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clust40PG',
            fields=[
                ('clust40pg', models.CharField(max_length=264, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operons',
            fields=[
                ('operon_ID', models.CharField(max_length=264, primary_key=True, serialize=False, unique=True)),
                ('operon_IM', models.ImageField(upload_to='static/ecis_web_first_app/uploaded_img')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('genome_ID_x', models.CharField(max_length=264, primary_key=True, serialize=False, unique=True)),
                ('phylum', models.CharField(max_length=264)),
                ('species', models.CharField(max_length=264)),
                ('genus', models.CharField(max_length=264)),
                ('strain', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='EcisDataBase',
            fields=[
                ('scaffold', models.CharField(max_length=264)),
                ('gene_id', models.CharField(max_length=264, primary_key=True, serialize=False, unique=True)),
                ('locus_tag_x', models.CharField(max_length=264)),
                ('start_coord_x', models.CharField(max_length=264)),
                ('end_coord_x', models.CharField(max_length=264)),
                ('core_whole', models.CharField(max_length=264)),
                ('len_aa', models.CharField(max_length=264)),
                ('clust40pg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecis_web_first_app.Clust40PG')),
                ('genome_ID_x', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecis_web_first_app.Species')),
                ('operon_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecis_web_first_app.Operons')),
            ],
        ),
    ]
