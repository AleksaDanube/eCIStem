from django.db import models

#Create your models here.
class Clust40PG(models.Model):
    clust40pg = models.CharField(max_length=264, unique=True, primary_key=True)
    def __str__(self):
        return self.clust40pg
class Operons(models.Model):
    operon_ID = models.CharField(max_length=264, unique=True, primary_key=True)
    index_ID = models.IntegerField()
    operon_IM = models.ImageField(upload_to='static/ecis_web_first_app/uploaded_img')
    def __str__(self):
        return self.operon_ID
class Species(models.Model):
    genome_ID_x = models.CharField(max_length=264, unique=True, primary_key=True)
    phylum = models.CharField(max_length=264, unique=False)
    species = models.CharField(max_length=264, unique=False)
    genus = models.CharField(max_length=264, unique=False)
    strain = models.CharField(max_length=264, unique=False)
    def __str__(self):
        return self.genome_ID_x

class EcisDataBase(models.Model):
    genome_ID_x = models.ForeignKey(Species, on_delete=models.CASCADE)
    scaffold = models.CharField(max_length=264, unique=False)
    gene_id = models.CharField(max_length=264, unique=True, primary_key=True)
    locus_tag_x = models.CharField(max_length=264, unique=False)
    start_coord_x = models.IntegerField(unique=False)
    end_coord_x = models.IntegerField(unique=False)
    operon_ID = models.ForeignKey(Operons, on_delete=models.CASCADE)
    core_whole = models.CharField(max_length=264, unique=False)
    clust40pg = models.ForeignKey(Clust40PG, on_delete=models.CASCADE)
    len_aa = models.IntegerField(unique=False)


    def __str__(self):
        return str(self.gene_id)

class PfamDb(models.Model):
    gene_id = models.ForeignKey(EcisDataBase, on_delete=models.CASCADE)
    genome_ID = models.ForeignKey(Species, on_delete=models.CASCADE)
    pfam_id = models.CharField(max_length=264, unique=False)
    pfam_name = models.CharField(max_length=264, unique=False)
    pfam_length = models.CharField(max_length=264, unique=False)
    pfam_query_start = models.IntegerField(unique=False)
    pfam_query_end = models.IntegerField(unique=False)
    pfam_evalue = models.CharField(max_length=264, unique=False)
    def __str__(self):
        return str(self.pfam_id)
