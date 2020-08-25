import os
import pandas
from decimal import Decimal
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecis_web_project.settings')

import django
# Import settings
django.setup()


from ecis_web_first_app.models import Clust40PG, Operons, Species, EcisDataBase, PfamDb


db_ecis = pandas.read_csv('database_for_website_may_2020.csv')
db_ecis = db_ecis.drop_duplicates('gene_ID_string')
db_ecis = db_ecis.fillna('NA')
db_ecis = db_ecis.applymap(str)
db_ecis.to_csv('new_db.csv')
db_pfam = pandas.read_csv('ecis_with_pfam.csv')
db_pfam = db_pfam[db_pfam['pfam_id'].notna()]
#db_ecis = db_ecis.drop_duplicates('gene_ID_string')
db_pfam = db_pfam.fillna('NA')
db_pfam = db_pfam.applymap(str)
db_pfam.to_csv('new_pfam_db.csv')
print('start population')
prev_operon_ID = 'NA'
i=0
for index, row in db_ecis.iterrows():
    #print(str(row['40_percent_ID_group_x']))
    aa_entry = row['len_aa']
    if aa_entry !='NA':
        aa_entry = int(row['len_aa'][:-2])
    else:
        aa_entry = round((int(row['end_coord_x']) - int(row['start_coord_x'])+1)/3)
    if row['clust_ID_x'] != prev_operon_ID:
        i=i+1
        prev_operon_ID = row['clust_ID_x']
    clg = Clust40PG.objects.get_or_create(clust40pg = row['40_percent_ID_group_x'])[0]
    clg.save()
    opr = Operons.objects.get_or_create(operon_ID = row['clust_ID_x'],
                                        index_ID = i,
                                        operon_IM = "ecis_web_first_app/static_ims/operonID_"+row['clust_ID_x']+".jpeg")[0]
    opr.save()

    spc = Species.objects.get_or_create(genome_ID_x = row['genome_ID_x'],
                                        phylum = row['Phylum'],
                                        species = row['Species_x'],
                                        genus = row['Genus'],
                                        strain = row['Strain'])[0]
    spc.save()
    #print(row['gene_ID_string'])
    edb = EcisDataBase.objects.get_or_create(genome_ID_x = spc,
                                        scaffold = row['scaffold'].replace('_', ' '),
                                        gene_id = row['gene_ID_string'],
                                        locus_tag_x = row['locus_tag_x'].replace('_', ' '),
                                        start_coord_x = int(row['start_coord_x']),
                                        end_coord_x = int(row['end_coord_x']),
                                        operon_ID = opr,
                                        core_whole = row['core_whole'].replace('_', ' '),
                                        clust40pg = clg,
                                        len_aa = aa_entry)[0]


    edb.save()
    temp_df = db_pfam.loc[db_pfam['gene_ID_string']==row['gene_ID_string']]
    #print(temp_df)
    if temp_df.size > 0:
        for index2, row2 in temp_df.iterrows():
            #print ('loop')
            aa_entry2 = row2['pfam_length']
            if aa_entry2 !='NA':
                aa_entry2 = int(row2['pfam_length'][:-2])
            else:
                aa_entry2 = int(row2['query_end'][:-2]) -  int(row2['query_start'][:-2])
            pfm = PfamDb.objects.get_or_create(gene_id = edb,
                                              genome_ID = spc,
                                              pfam_id = row2['pfam_id'],
                                              pfam_name = row2['pfam_name'],
                                              pfam_length = aa_entry2,
                                              pfam_query_start = int(row2['query_start'][:-2]),
                                              pfam_query_end = int(row2['query_end'][:-2]),
                                              pfam_evalue = str("{:.2E}".format(Decimal(row2['evalue']))))[0]
            #print(str("{:.2E}".format(Decimal(row2['evalue']))))
            pfm.save()

# for index, row in db_pfam.iterrows():
#     pfm = PfamDb.objects.get_or_create(gene_id = row['gene_oid'],
#                                       genome_ID = row['genome_ID'],
#                                       pfam_id = row['pfam_id'],
#                                       pfam_name = row['pfam_name'],
#                                       pfam_length = row['pfam_length'],
#                                       pfam_query_start = row['query_start'],
#                                       pfam_query_end = row['query_end'],
#                                       pfam_evalue = row['evalue'])[0]
#     pfm.save()
print('population completed')
