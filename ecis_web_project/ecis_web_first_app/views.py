from django.shortcuts import render
from django.http import HttpResponse
from .models import Clust40PG,Operons,Species,EcisDataBase,PfamDb
from PIL import Image
import shutil
# Create your views here.
def homepage(request):
	phylums_list = []
	phylums = Species.objects.all()
	#phylums_dict = {'phylum_list':phylums}
	#print(list(phylums))
	phylum_values = phylums.values('phylum')
	#print(phylum_values)
	for item in phylum_values:
		#print(item)
		phylums_list.append(item['phylum'])
	#print(set(phylums_list))
	# for item in genoms:
	# 	opid.extend(Operons.objects.filter(operon_ID__exact=item.operon_ID))
	#
	# #print(opid)
	phylums_dict = {"phylums_list":set(phylums_list)}
	return render(request, 'ecis_web_first_app/homepage.html', phylums_dict)
def header0(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header0.html', operons_dict)
def header1(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header1.html', operons_dict)
def header2(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header2.html', operons_dict)
def header3(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header3.html', operons_dict)
def header4(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header4.html', operons_dict)
def header5(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header5.html', operons_dict)
def header6(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header6.html', operons_dict)
def header7(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header7.html', operons_dict)
def header8(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header8.html', operons_dict)
def header9(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header9.html', operons_dict)
def header10(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header10.html', operons_dict)
def header11(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header11.html', operons_dict)
def header12(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header12.html', operons_dict)
def header13(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header13.html', operons_dict)
def header14(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header14.html', operons_dict)
def header15(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header15.html', operons_dict)
def header16(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header16.html', operons_dict)
def header17(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header17.html', operons_dict)
def header18(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header18.html', operons_dict)
def header19(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header19.html', operons_dict)
def header20(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header20.html', operons_dict)
def header21(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header21.html', operons_dict)
def header22(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header22.html', operons_dict)
def header23(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header23.html', operons_dict)
def header24(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header24.html', operons_dict)
def header25(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header25.html', operons_dict)
def header26(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header26.html', operons_dict)
def header27(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header27.html', operons_dict)
def header28(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header28.html', operons_dict)
def header29(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header29.html', operons_dict)
def header30(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header30.html', operons_dict)
def header31(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header31.html', operons_dict)
def header32(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header32.html', operons_dict)
def header33(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header33.html', operons_dict)
def header34(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header34.html', operons_dict)
def header35(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header35.html', operons_dict)
def header36(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header36.html', operons_dict)
def header37(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header37.html', operons_dict)
def header38(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header38.html', operons_dict)
def header39(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header39.html', operons_dict)
def header40(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header40.html', operons_dict)
def header41(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header41.html', operons_dict)
def header42(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header42.html', operons_dict)
def header43(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header43.html', operons_dict)
def header44(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header44.html', operons_dict)
def header45(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header45.html', operons_dict)
def header46(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header46.html', operons_dict)
def header47(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header47.html', operons_dict)
def pfams_det(request, gene):
	pfams = []
	pfams = PfamDb.objects.filter(gene_id__exact=gene)
	print(pfams.values('genome_ID'))

	pfams_dict = {"pfam_list":pfams,"gene_id":gene}
	return render(request,'ecis_web_first_app/pfams_det.html',pfams_dict)

def PhylumSearch(request, phylum_name):
	genoms = []
	search_term = ''
	opid = []
	#search_term = request.GET.get('q')
	#print('search_term is ' +search_term)
	phyls = Species.objects.filter(phylum__exact = phylum_name)
	#print(phyls.values('phylum'))
	gmid_values = phyls.values('genome_ID_x')
	#print(phyls_values)
	for item in gmid_values:
		genoms.extend(EcisDataBase.objects.filter(genome_ID_x=item['genome_ID_x']))
	print(genoms)
	for item in genoms:
		opid.extend(Operons.objects.filter(operon_ID__exact=item.operon_ID))

	#print(opid)
	phyls_dict = {"phyls_list":phyls[0], "opids_list":set(opid)}
	return render(request, 'ecis_web_first_app/phylumsearch.html', phyls_dict)

def operonsearch(request):
	search_term = request.GET.get('q')
	print('search_term is ' +search_term)
	try:
		operons = Operons.objects.get(operon_ID = search_term)
		ops_dict = {"operon_list":operons}
	except Operons.DoesNotExist:
		ops_dict = {"operon_list":[]}


	return render(request, 'ecis_web_first_app/operonsearch.html', ops_dict)

def operon_det(request, operon_id):
	search_term = ''
	opid = ''
	genes = ''
	species = ''
	opid = Operons.objects.get(operon_ID__exact=operon_id)
	genes = EcisDataBase.objects.filter(operon_ID=operon_id)
	genes_values = genes.values('genome_ID_x')
	scaffold = genes.values('scaffold')[0]
	scaffold['scaffold'] = scaffold['scaffold'].replace('_', ' ')
	print (scaffold)
	species = Species.objects.get(genome_ID_x=genes_values[0]['genome_ID_x'])
	#print(EcisDataBase.objects.filter(genome_ID_x__exact=str(genes.values('genome_ID_x')).values('operon_ID')))
	operon_dict = {"genes_list": genes, "species_list": species, "opid":opid, "scaffold":scaffold}
	return render(request, 'ecis_web_first_app/operon_det.html', operon_dict)

def cluster_det(request, cluster_id):
	print('clust is ' + cluster_id)
	clst = Clust40PG.objects.get(clust40pg__exact=cluster_id)
	genes = EcisDataBase.objects.filter(clust40pg__exact=cluster_id)
	clust_dict = {"genes_list_within_clust": genes, "clst40":clst}
	return render(request, 'ecis_web_first_app/cluster_det.html', clust_dict)
